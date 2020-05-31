from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response


def application(environ, start_response):
    req = Request(environ)
    body = 'Hello World'

    resp = Response(body, mimetype='text/plain')
    return resp(environ, start_response)


if __name__ == "__main__":
    run_simple('localhost', 5000, application)
