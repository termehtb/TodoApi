import json

import redis

rds =redis.StrictRedis(port=6379, db=0)

class Red:
    def set(cache_key, data):
        data = json.dumps(data)
        rds.set(cache_key, data)
        return True

    def get(cache_key):
        cache_data = rds.get(cache_key)
        if not cache_key:
            return None
        cache_data = json.loads(cache_data)
        return cache_data
