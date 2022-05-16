import os

from instance.config import SECRET_KEY




class Config:

    SECRET_KEY = '1234567YGFDZSAzXCVBN'






class ProdConfig(Config):




    pass



class DevConfig(Config):


    DEBUG = True




class TestConfig(Config):



      DEBUG = True




config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}
            