import os

from instance.config import SECRET_KEY




class Config:

    SECRET_KEY = '1234567YGFDZSAzXCVBN'









class ProdConfig(Config):






    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    DEBUG = True





class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings

    '''



    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)


    DEBUG = True


class TestConfig(Config):



      DEBUG = True




config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}
            