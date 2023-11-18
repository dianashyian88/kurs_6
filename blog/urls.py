from django.urls import path
from blog.apps import BlogConfig
from django.views.decorators.cache import cache_page
from blog.views import BlogDetailView, BlogListView, home


app_name = BlogConfig.name

urlpatterns = [
    #path('', BlogListView.as_view(), name='home'),
    path('', home, name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),

]
