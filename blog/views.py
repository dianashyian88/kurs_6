from django.views.generic import ListView, DetailView
from blog.models import Blog
from distribution.models import Distribution, Client
from django.shortcuts import render
from blog.utils import get_blogs_cache


class BlogListView(ListView):
    model = Blog
    template_name = 'distribution/home.html'


    def get_queryset(self, *args, **kwargs):
        queryset = self.model._default_manager.order_by('-public_date')[:3]
        return queryset

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

def home(request):
    client = len(Client.objects.order_by('email').distinct('email'))
    #object_list = Blog.objects.order_by('-public_date')
    object_list = get_blogs_cache()
    distribution = len(Distribution.objects.all())
    distribution_active = len(Distribution.objects.filter(is_active=True))
    context = {
        'object_list': object_list[:3],
        'distribution': distribution,
        'distribution_active': distribution_active,
        'client': client
    }
    return render(request, 'distribution/home.html', context)
