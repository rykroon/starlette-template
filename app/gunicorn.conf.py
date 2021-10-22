import os


bind = os.getenv('GUNICORN_BIND', '0.0.0.0')

loglevel = os.getenv('GUNICORN_LOGLEVEL', 'info')

reload = os.getenv('GUNICORN_RELOAD', False)

workers = os.getenv('GUNICORN_WORKERS', 2 * os.cpu_count() + 1)

worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'uvicorn.workers.UvicornWorker')