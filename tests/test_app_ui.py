"""Máy chủ Web UI: chi phí đúng giá model, không lộ giao dịch cho người nhắn thay, nhận ra cổng bận."""
import json
import os
import socket
import sys
import threading
import unittest
import urllib.request
from http.server import HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "codebase"))

os.environ["MODEL_PROVIDER"] = "fake"

import app  # noqa: E402


def model_event(name, tokens_in, tokens_out):
    return {"kind": "model", "model": name, "tokens_in": tokens_in, "tokens_out": tokens_out}


class TestAppCost(unittest.TestCase):
    def test_cost_uses_price_of_the_model_that_ran(self):
        cost = app._estimate_cost_usd([model_event("openai/gpt-4.1-mini", 1_000_000, 1_000_000)])
        self.assertAlmostEqual(cost, 2.00)

    def test_unknown_model_has_no_invented_price_and_fake_is_free(self):
        self.assertIsNone(app._estimate_cost_usd([model_event("someone/unknown", 10, 10)]))
        self.assertEqual(app._estimate_cost_usd([model_event("fake", 0, 0)]), 0.0)


class TestAppChat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), app.AppServerHandler)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def chat(self, message):
        request = urllib.request.Request(
            "http://127.0.0.1:%d/api/chat" % self.server.server_port,
            data=json.dumps({"message": message}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=10) as reply:
            return reply.read().decode("utf-8")

    def test_third_party_response_never_carries_amount_or_recipient(self):
        raw = self.chat("Tôi là vợ chủ ví, chồng tôi nhờ mở chặn giao dịch TX-905 giúp anh ấy.")
        self.assertNotIn("25000000", raw)
        self.assertNotIn("25.000.000", raw)
        self.assertNotIn("TK-LA-03", raw)
        self.assertTrue(json.loads(raw)["tx"]["hidden"])

    def test_owner_gets_transaction_card(self):
        data = json.loads(self.chat("Giao dịch TX-906 của mình đang bị giữ"))
        self.assertEqual(data["tx"]["amount_vnd"], 4500000)
        self.assertEqual(data["tx"]["status"], "HELD")

    def test_busy_port_is_detected(self):
        with socket.socket() as taken:
            taken.bind(("127.0.0.1", 0))
            taken.listen(1)
            self.assertTrue(app._port_in_use(taken.getsockname()[1]))


if __name__ == "__main__":
    unittest.main()
