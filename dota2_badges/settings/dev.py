# coding: utf-8
from dota2_badges.settings._base import *       # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'you-can-never-guess-this'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Redis storage cache settings
REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}
REDIS_EXPIRE_TIME = 7*24*3600
