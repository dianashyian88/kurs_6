from django.urls import path
from blog.apps import BlogConfig
from django.views.decorators.cache import cache_page
from blog.views import BlogDetailView, BlogListView


app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),

]
