from django.conf.urls import url
from badge.views import render_solo_mmr_badge, render_team_mmr_badge, render_estimate_mmr_badge


urlpatterns = [
    url(r'^(?P<steam_id>[0-9]+)/mmr/solo.svg$', render_solo_mmr_badge),
    url(r'^(?P<steam_id>[0-9]+)/mmr/team.svg$', render_team_mmr_badge),
    url(r'^(?P<steam_id>[0-9]+)/mmr/estimate.svg$', render_estimate_mmr_badge),
]
