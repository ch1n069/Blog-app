import os

from instance.config import SECRET_KEY




class Config:

    SECRET_KEY = '1234567YGFDZSAzXCVBN'



    DEBUG = True    






class ProdConfig(Config):






    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:newpassword@localhost/blog'

    DEBUG = True

    pass





class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings

    '''



    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:newpassword@localhost/blog'


    DEBUG = True


class TestConfig(Config):



      DEBUG = True




config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}
            