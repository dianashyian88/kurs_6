from django.urls import path
from distribution.apps import DistributionConfig
from django.views.decorators.cache import cache_page
from distribution.views import HomeListView


app_name = DistributionConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    #path('contacts/', contacts, name='contacts'),
    #path('categories/', categories, name='categories'),

]