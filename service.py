from datetime import datetime
import io
import time
import threading
import logging
from wsgiref.validate import validator
from wsgiref.simple_server import make_server

EXCHANGE_FILE = "./exchange.dat"


def update_exchange_file():
    """
    Writes the current date and time every 10 seconds into the exchange file.
    The file is created if it does not exist.
    """
    logging.info("Will update to exchange file...")
    while True:
        with io.open(EXCHANGE_FILE, "w") as f:
            f.write(datetime.now().isoformat())
        time.sleep(10)


def simple_app(environ, start_response):
    """
    Read the content of the exchange file and return it.
    """
    start_response('200 OK', [('Content-type', 'text/plain')])
    with io.open(EXCHANGE_FILE) as f:
        return [f.read().encode('utf-8')]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    t = threading.Thread(target=update_exchange_file)
    t.start()

    httpd = make_server('', 80, simple_app)
    logging.info("Listening on port 80...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        t.join(timeout=1)