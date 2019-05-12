from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('.collections')
        config.include('.routes')
        config.include('cornice')
        config.include('.views.api', route_prefix='/api')
    return config.make_wsgi_app()
