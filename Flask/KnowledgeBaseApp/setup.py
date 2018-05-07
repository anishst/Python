# http://flask.pocoo.org/docs/1.0/patterns/distribute/

from setuptools import setup

setup(
    name='ATS KnowledgeBase',
    version='Beta',
    long_description=__doc__,
    packages=['KB'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)