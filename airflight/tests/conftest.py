import os

import mongomock
import pytest
from pyramid import testing
from pyramid.paster import get_appsettings
from pyramid.threadlocal import get_current_registry
from webtest import TestApp
from mock import patch
from airflight import main

here = os.path.dirname(__file__)
settings_file = os.path.join(here, '../../', 'testing.ini')


@pytest.fixture(scope='module', autouse=True)
def settings():
    settings = get_appsettings(settings_file, name='main')
    get_current_registry().settings = dict(settings)
    return settings

@pytest.fixture(scope='session')
def app(request):
    with patch('airflight.collections.base.MongoClient', mongomock.MongoClient):

        _settings = get_appsettings(settings_file, name='main')

        config = testing.setUp(settings=_settings)

        config.include('airflight.collections')

        _app = main(_settings.global_conf, **_settings)
        test_app = TestApp(_app)

        yield test_app

