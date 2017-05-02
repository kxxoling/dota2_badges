# coding: utf-8
import redis
from django.conf import settings


r = redis.StrictRedis(**settings.REDIS)


def get_mmr(steam_id, type_='solo'):
    return r.get('%d%s' % (steam_id, type_))


def set_mmr(steam_id, type_, mmr):
    return r.setex('%d%s' % (steam_id, type_), settings.REDIS_EXPIRE_TIME, mmr)

