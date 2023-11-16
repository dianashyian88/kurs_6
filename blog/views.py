from django.views.generic import ListView, DetailView
from blog.models import Blog


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

