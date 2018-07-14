import json, time

from django.shortcuts import render
from django.http import JsonResponse

from mcstatus import MinecraftServer

from common.misc_storage import MiscStorage

CACHE_FOR = 5 # 5 seconds


def status(request):
    result = dict()

    ms_key = 'server_status.cache'
    cache_raw = MiscStorage.get(ms_key, False)
    if cache_raw:
        cache = json.loads(cache_raw)
        if 'timestamp' in cache and type(cache['timestamp']) is int and int(time.time()) - cache['timestamp'] <= CACHE_FOR:
            result = cache['data']
            result['cached'] = True
            return JsonResponse(result)

    srv = MinecraftServer('play.bbyaworld.com', 25565)

    try:
        status = srv.status()
        
        result['online'] = True
        result['status'] = 'success'

        result['players'] = {
            'online': status.players.online,
            'max': status.players.max,
            'list': [p.name for p in status.players.sample],
        }

    except Exception as e:
        result['online'] = False
        result['status'] = 'error'

        # pylint: disable=no-member

        if hasattr(e, 'strerror') and e.strerror:
            result['error'] = e.strerror
        elif hasattr(e, 'message') and e.message:
            result['error'] = e.message
        else:
            result['error'] = str(e)
        
    MiscStorage.set(ms_key, json.dumps({
        'timestamp': int(time.time()),
        'data': result,
    }))

    result['cached'] = False

    return JsonResponse(result)