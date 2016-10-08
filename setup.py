try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'sam_broadcaster',
    'version': '0.1',
    'description': 'SAM Broadcaster Connector',
    'url': 'https://github.com/IamMrCupp/sam_broadcaster-python',
    'author': 'Aaron Cupp',
    'author_email': 'mrcupp@mrcupp.com',
    'license': 'GPL-3.0+',
    'packages': ['sam_broadcaster'],
    'scripts': []
}

setup(**config)
