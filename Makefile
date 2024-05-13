get_req:
	pip freeze > requirements.txt

run_all_tests:
	pytest .\Selenium\code\test.py

run_test:
	pytest .\Selenium\code\test.py::$(test_name) --capture=no --setup-show