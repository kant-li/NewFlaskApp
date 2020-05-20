"""
redis ops
"""

import redis

from config import config

pool = redis.ConnectionPool(
    host=config.REDIS_ADDRESS, port=config.REDIS_PORT, decode_responses=True
)


####
# redis 操作
####
def redis_add_str(name: str, value: str, ex: int = None):
    r = redis.Redis(connection_pool=pool)
    r.set(name=name, value=value, ex=ex)


def redis_get_str(name: str):
    r = redis.Redis(connection_pool=pool)
    return r.get(name)


def redis_delete_str(name: str):
    r = redis.Redis(connection_pool=pool)
    r.delete(name)
