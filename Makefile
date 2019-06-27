auth:
	python -m telegram.client
serve:
	FLASK_APP=telegfeed.py FLASK_ENV=development flask run
