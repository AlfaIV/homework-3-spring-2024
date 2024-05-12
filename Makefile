GetReq:
	pip freeze > requirements.txt

pytest --setup-show
pytest --setup-show --capture=no
pytest .\Selenium\code\test_navbar.py::testRedirectSideButton --capture=no --setup-show