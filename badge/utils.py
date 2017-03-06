# coding: utf-8
import requests
import badge.cache as cache


def request_profile(steam_id):
    data = requests.get('https://api.opendota.com/api/players/%d' % steam_id)
    return data


def get_mmr(steam_id):
    cached_mmr = cache.get_mmr(steam_id)
    if cached_mmr:
        return cached_mmr
    profile = request_profile(steam_id)
    print(profile)
    mmr = profile.json().get('solo_competitive_rank', None)
    cache.set_mmr(steam_id, mmr)
    return mmr
