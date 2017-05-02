# coding: utf-8
import requests
import badge.cache as cache


def request_profile(steam_id):
    data = requests.get('https://api.opendota.com/api/players/%d' % steam_id)
    return data


def get_mmr(steam_id, type_='solo'):
    cached_mmr = cache.get_mmr(steam_id, type_=type_)
    if cached_mmr:
        return cached_mmr
    profile = request_profile(steam_id)
    data = profile.json()
    solo_mmr = data.get('solo_competitive_rank', None)
    team_mmr = data.get('competitive_rank', None)
    estimate_mmr = data.get('mmr_estimate', {}).get('estimate', None)
    if type_ == 'solo':
        mmr = solo_mmr
    elif type_ == 'team':
        mmr = team_mmr
    else:
        mmr = estimate_mmr
    cache.set_mmr(steam_id, 'solo', solo_mmr)
    cache.set_mmr(steam_id, 'team', team_mmr)
    cache.set_mmr(steam_id, 'estimate', estimate_mmr)
    return mmr
