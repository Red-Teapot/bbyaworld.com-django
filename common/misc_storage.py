from .models import MiscStorageEntry

class MiscStorage():

    @staticmethod
    def set(key: str, value: str):
        try:
            entry = MiscStorageEntry.objects.get(key=key)  # pylint: disable=no-member
            entry.value = value
        except:
            entry = MiscStorageEntry(key=key, value=value)
        entry.save()
    
    @staticmethod
    def get(key: str, default: str = None):
        try:
            obj = MiscStorageEntry.objects.get(key=key)  # pylint: disable=no-member
            return obj.value
        except:
            return default
