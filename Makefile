test-deps:
	@pip install -r test-requirements.txt

test: test-deps
	@py.test .

run:
	@honcho start
