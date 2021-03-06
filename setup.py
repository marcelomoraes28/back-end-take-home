import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_retry',
    'pymongo==3.8.0',
    'cornice==3.5.1',
    'colander==1.7.0',
    'cornice-swagger==0.7.0',
    'pyramid-auto-env==0.1.2'
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest >= 3.7.4',
    'pytest-cov',
    'mongomock==3.16.0',
    'mock==3.0.5'
]

setup(
    name='airflight',
    version='1.0',
    description='airflight',
    long_description=README,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = airflight:main',
        ],
        'console_scripts': [
            'initialize_airflight_db=airflight.scripts.initialize_db:main',
        ],
    },
)
