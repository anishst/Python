# http://flask.pocoo.org/docs/0.12/config/#configuration-basics

class BaseConfig(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///KnowledgeBase.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = True

#class ProductionConfig(Config):
    #DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


