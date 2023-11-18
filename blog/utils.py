from blog.models import Blog
from config.settings import CACHE_ENABLED
from django.core.cache import cache

def get_blogs_cache():
    key = 'blog_list'
    blog_list = Blog.objects.order_by('-public_date')
    if CACHE_ENABLED:
        cache_blog = cache.get(key)
        if cache_blog is None:
            cache_blog = blog_list
            cache.set(key, cache_blog)
        return cache_blog
    else:
        return blog_list
