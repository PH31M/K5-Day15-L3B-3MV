# TUỲ CHỌN cho máy có sẵn make (Windows không có make chạy thẳng `python ...`).
PY ?= python3
run: ; $(PY) run.py
check: ; $(PY) run.py check
test: ; $(PY) -m unittest discover -s tests -v
verify:
	$(PY) -m unittest discover -s tests -v
	$(PY) run.py check
	$(PY) evidence/mine_reviews.py --recount
	$(PY) evidence/survey/analyze_survey.py
freeze-cp2: ; $(PY) tests/freeze_cp2.py
eval: ; $(PY) run.py eval
eval-try: ; $(PY) run.py eval --try
score: ; $(PY) run.py score $(RUN)
simulate: ; $(PY) run.py simulate
simulate-try: ; $(PY) run.py simulate --try
.PHONY: run check test verify freeze-cp2 eval eval-try score simulate simulate-try
