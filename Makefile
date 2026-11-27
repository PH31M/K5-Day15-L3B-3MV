# TUỲ CHỌN cho máy có sẵn make (Windows không có make chạy thẳng `python ...`).
PY ?= python3
run: ; $(PY) run.py
check: ; $(PY) run.py check
test: ; $(PY) -m unittest discover -s tests -v
verify:
	$(PY) -m unittest discover -s tests -v
	$(PY) run.py check
	$(PY) evidence/mine_reviews.py --recount
freeze-cp2:
	$(PY) -c "import hashlib, json, re; from pathlib import Path; r=Path('.'); m=hashlib.sha256((r/'eval/metric_spec.yaml').read_text(encoding='utf-8').encode()).hexdigest(); s=re.search(r'(## §7\..*?)(?=\n## §8\.)', (r/'spec.md').read_text(encoding='utf-8'), re.S).group(1).strip(); sh=hashlib.sha256(s.encode()).hexdigest(); (r/'eval/.cp2_lock.json').write_text(json.dumps({'metric_spec_sha256': m, 'spec_sec7_sha256': sh}, indent=2), encoding='utf-8'); print('Frozen CP2 hashes -> eval/.cp2_lock.json')"
eval: ; $(PY) run.py eval
eval-try: ; $(PY) run.py eval --try
score: ; $(PY) run.py score $(RUN)
simulate: ; $(PY) run.py simulate
simulate-try: ; $(PY) run.py simulate --try
.PHONY: run check test verify freeze-cp2 eval eval-try score simulate simulate-try
