import redis

"""
键值对操作（set()、get()、delete()、expire()、exists()）、
哈希表操作（hset()、hget()、hdel()）、
列表操作（lpush()、rpush()、lpop()、rpop()）、
集合操作（sadd()、srem()、smembers()）、
有序集合操作（zadd()、zrange()、zrem()）、
发布订阅操作（publish()、subscribe()）等。
"""


class RedisClient:
    def __init__(self, host, port, password=None, db=0):
        self.redis = redis.Redis(host=host, port=port, password=password, db=db)

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        self.redis.set(key, value, ex=ex, px=px, nx=nx, xx=xx)

    def get(self, key):
        return self.redis.get(key)

    def delete(self, *keys):
        return self.redis.delete(*keys)

    def expire(self, key, seconds):
        return self.redis.expire(key, seconds)

    def exists(self, key):
        return self.redis.exists(key)

    def hset(self, name, key, value):
        return self.redis.hset(name, key, value)

    def hget(self, name, key):
        return self.redis.hget(name, key)

    def hdel(self, name, *keys):
        return self.redis.hdel(name, *keys)

    def lpush(self, name, *values):
        return self.redis.lpush(name, *values)

    def rpush(self, name, *values):
        return self.redis.rpush(name, *values)

    def lpop(self, name):
        return self.redis.lpop(name)

    def rpop(self, name):
        return self.redis.rpop(name)

    def sadd(self, name, *values):
        return self.redis.sadd(name, *values)

    def srem(self, name, *values):
        return self.redis.srem(name, *values)

    def smembers(self, name):
        return self.redis.smembers(name)

    def zadd(self, name, *args, **kwargs):
        return self.redis.zadd(name, *args, **kwargs)

    def zrange(self, name, start, end, withscores=False):
        return self.redis.zrange(name, start, end, withscores=withscores)

    def zrem(self, name, *values):
        return self.redis.zrem(name, *values)

    def publish(self, channel, message):
        return self.redis.publish(channel, message)

    def subscribe(self, channel):
        pubsub = self.redis.pubsub()
        pubsub.subscribe(channel)
        return pubsub

    # 自定义方法
    def incr(self, key, amount=1):
        return self.redis.incr(key, amount)

    def decr(self, key, amount=1):
        return self.redis.decr(key, amount)
