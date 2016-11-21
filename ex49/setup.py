try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Heidi',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'pancakeinacakepan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts': []
    'name': 'ex49'
}

setup(**config)
