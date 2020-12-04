from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response


class WebApp(object):

    def __init__(self):
        pass

    def dispatch_request(self, request):
        return Response('Hello World')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)

        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(host='localhost', port=5000):
    app = WebApp()
    return app


if __name__ == "__main__":
    app = create_app()
    run_simple('localhost', 5000, app)
