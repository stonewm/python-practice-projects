from werkzeug.serving import run_simple


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', headers)
    return [b'Hello World']


if __name__ == "__main__":
    run_simple('localhost', 5000, application)
