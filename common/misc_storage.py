from .models import MiscStorageEntry

class MiscStorage():

    @staticmethod
    def put(key: str, value: str):
        entry = MiscStorageEntry(key=key, value=value)
        entry.save()
    
    @staticmethod
    def get(key: str, default: str = None):
        try:
            obj = MiscStorageEntry.objects.get(key=key)  # pylint: disable=no-member
            return obj.value
        except:
            return default
