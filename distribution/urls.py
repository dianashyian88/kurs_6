from django.urls import path
from distribution.apps import DistributionConfig
from django.views.decorators.cache import cache_page
from distribution.views import ClientListView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, DistributionListView, DistributionCreateView, \
    DistributionUpdateView, DistributionDeleteView, DistributionLogsListView
from blog.views import BlogListView


app_name = DistributionConfig.name

urlpatterns = [
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_form'),
    path('client_edit/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('distribution_list/', DistributionListView.as_view(), name='distribution_list'),
    path('distribution_create/', DistributionCreateView.as_view(), name='distribution_form'),
    path('distribution_edit/<int:pk>', DistributionUpdateView.as_view(), name='distribution_update'),
    path('distribution_delete/<int:pk>', DistributionDeleteView.as_view(), name='distribution_delete'),
    path('logs_list/', DistributionLogsListView.as_view(), name='logs_list'),

]
