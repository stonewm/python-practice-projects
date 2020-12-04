from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException


class WebApp(object):

    def __init__(self):
        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/users/<userid>', endpoint='userinfo')
        ])

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, args = adapter.match()
            # 根据endpoint,找到视图函数 on_endpointname，并且执行
            return getattr(self, 'on_'+endpoint)(request, **args)
        except HTTPException as ex:
            return ex

    def wsgi_app(self, environ, start_response):
        req = Request(environ)
        resp = self.dispatch_request(req)
        return resp(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def on_index(self, request):        
        return Response('index page')
    
    def on_userinfo(self, request, userid):
        return Response('Hello, {}'.format(userid))


def create_app(host='localhost', port=5000):
    app = WebApp()
    return app


if __name__ == "__main__":
    app = create_app()
    run_simple('localhost', 5000, app)
