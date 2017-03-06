# coding: utf-8
from django.shortcuts import render
from badge.utils import get_mmr


def render_badge(request, steam_id):
    steam_id = int(steam_id)
    mmr = get_mmr(steam_id)
    return render(request, 'badge.html', dict(mmr=mmr), 'image/svg+xml')
