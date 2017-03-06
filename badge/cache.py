# coding: utf-8
import redis
from django.conf import settings


r = redis.StrictRedis(**settings.REDIS)


def get_mmr(steam_id):
    return r.get(steam_id)


def set_mmr(steam_id, mmr):
    return r.setex(steam_id, settings.REDIS_EXPIRE_TIME, mmr)
