import os

from setuptools import setup

README = '''Python Google Reader Client Library'''

setup(name='py-gr-client',
      version='0.1',
      description='',
      long_description=README,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        ],
      author='Filia Tao',
      author_email='Filia.Tao@gmail.com',
      url='',
      keywords='google reader,client,feed',
      packages=['grclient'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'oauth2',
            ],
      tests_require=[
            'oauth2',
            ],
      )

