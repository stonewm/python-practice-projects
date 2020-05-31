from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.exceptions import HTTPException, NotFound
from jinja2 import Environment, FileSystemLoader
import os


class WebApp(object):
    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)
        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/users/<userid>', endpoint='userinfo')
        ])

        self.view_functions = {
            'index': self.on_index,
            'userinfo': self.on_userinfo
        }

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, args = adapter.match()
            return self.view_functions[endpoint](endpoint, **args)
        except HTTPException as e:
            return e

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def wsgi_app(self, environ, start_response):
        req = Request(environ)
        resp = self.dispatch_request(req)
        return resp(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def on_index(self, request):
        return self.render_template('index.html')

    def on_userinfo(self, request, userid):
        return self.render_template('user.html', userid=userid)


def create_app(host='localhost', port=5000, with_static=True):
    app = WebApp()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


if __name__ == "__main__":
    app = create_app()
    run_simple('localhost', 5000, app)
