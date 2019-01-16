#!/usr/bin/env python
"""Contains configurations for defferent environments"""
import os

#config.py
class Config(object):
    """Parent/default configutaion"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DB_NAME = "testdb"
    APP_SETTINGS = "testing"


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    APP_SETTINGS = "development"


class ProductionConfig(Config):
    """Development configuration"""
    DEBUG = False
    TESTING = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
