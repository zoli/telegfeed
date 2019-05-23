auth:
	python telegram/client.py
serve:
	FLASK_APP=telegfeed.py FLASK_ENV=development flask run
