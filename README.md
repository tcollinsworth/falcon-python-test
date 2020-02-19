# falcon pyton test

Send raw byte response to http request.

See things.py

Just run the code and it will start a server. Open browser on http://localhost:8000/things


# gunicorn command line example

```
$ gunicorn things:app
```

# wsgi command line examples

```
$ LD_LIBRARY_PATH=/home/troy/anaconda3/lib uwsgi --version

$ LD_LIBRARY_PATH=/home/troy/anaconda3/lib uwsgi --http :9090 --wsgi-file fubar.py

$ LD_LIBRARY_PATH=/home/troy/anaconda3/lib uwsgi --http localhost:9090 --wsgi-file fubar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

$ LD_LIBRARY_PATH=/home/troy/anaconda3/lib uwsgi --http :9090 --wsgi-file things.py

$ LD_LIBRARY_PATH=/home/troy/anaconda3/lib uwsgi --http :9090 --wsgi-file fubar.py
```
