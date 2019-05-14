from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.add_static_view('static', 'static',
                               cache_max_age=3600)
        config.include('cornice')
        config.include('.collections')
        config.include('.routes')
        config.include('.views.api', route_prefix='/api')
        config.include('cornice_swagger')
    return config.make_wsgi_app()
