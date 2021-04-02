web: gunicorn WebProjectSpotify.wsgi --log-file -
release: python3 WebProjectSpotify/manage.py migrate
runs: python3 WebProjectSpotify/manage.py runserver
