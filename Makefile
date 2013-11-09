deps:
	@pip install -r requirements.txt

test-deps:
	@pip install -r test-requirements.txt

test: test-deps
	@py.test .

run: deps
	@honcho start
