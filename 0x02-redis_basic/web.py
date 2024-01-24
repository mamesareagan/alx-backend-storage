#!/usr/bin/env python3
''' Task 5 '''


import redis
import requests
import time
from functools import wraps


redis_client = redis.Redis()


def track_url_access_count(url):
    ''' Decorator to track URL access count in Redis.
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            redis_client.incr(f"count:{url}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@track_url_access_count("http://slowly.robertomurray.co.uk")
def get_page(url: str) -> str:
    ''' get HTML content of a URL and cache it for 10 seconds.
    '''
    cache_content = redis_client.get(url)
    if cache_content:
        return cache_content.decode("utf-8")


    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        redis_client.setex(url, 10, content)
        return content


    return ""


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    for _ in range(5):
        content = get_page(url)
        print(content[:100])
        time.sleep(1)


    access_count = redis_client.get(f"count:{url}")
    access_count = int(access_count) if access_count is not None else 0
    print(f"URL accessed {int(access_count)} time.")
