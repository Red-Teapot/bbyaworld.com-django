import urllib.request, json

class DynmapMarkup(object):
    def __init__(self, url):
        self._url = url
    
    def load(self):
        with urllib.request.urlopen(self._url) as response:
            raw_data = response.read()
            json_data = json.loads(raw_data.decode('utf8'))

            self._data = json_data
    
    @property
    def data(self):
        if hasattr(self, '_data'):
            return self._data
        else:
            raise Exception('Data is not loaded!')