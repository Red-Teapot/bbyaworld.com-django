from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from .scoreboard import Scoreboard


def index(request):
    rcon_settings = settings.SECRETS['mc']['rcon']
    response = ''

    with Scoreboard(rcon_settings['host'], rcon_settings['password'], port=rcon_settings['port']) as scoreboard:
        response += str(scoreboard.get_list_for_player('.PPWheat')) + '<br />'
        response += str(scoreboard.get_list_for_player('.PPCoal')) + '<br />'
        response += str(scoreboard.get_list_for_player('.PPAlm')) + '<br />'
        response += str(scoreboard.get_list_for_player('.expMarket')) + '<br />'
    return HttpResponse(response);