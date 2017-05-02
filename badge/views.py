# coding: utf-8
from django.shortcuts import render
from badge.utils import get_mmr


def render_badge(request, steam_id, type_):
    steam_id = int(steam_id)
    mmr = get_mmr(steam_id, type_)
    return render(request, 'badge.html', dict(mmr=mmr), 'image/svg+xml')


def render_solo_mmr_badge(request, steam_id):
    return render_badge(request, steam_id, 'solo')


def render_team_mmr_badge(request, steam_id):
    return render_badge(request, steam_id, 'team')


def render_estimate_mmr_badge(request, steam_id):
    return render_badge(request, steam_id, 'estimate')

