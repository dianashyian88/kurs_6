from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView,  UpdateView, DeleteView
from distribution.models import Distribution, Client
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.http import Http404


class ClientListView(ListView):
    model = Client
    template_name = 'distribution/client_list.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('name', 'description', 'email', 'distribution_id')
    success_url = reverse_lazy('distribution:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'description', 'email', 'distribution_id')
    success_url = reverse_lazy('distribution:client_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.save()

        return super().form_valid(form)


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('distribution:client_list')

class DistributionListView(ListView):
    model = Distribution
    template_name = 'distribution/distribution_list.html'

class DistributionCreateView(LoginRequiredMixin, CreateView):
    model = Distribution
    fields = ('name', 'start_datetime', 'end_datetime', 'frequency', 'message_id')
    success_url = reverse_lazy('distribution:distribution_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class DistributionUpdateView(LoginRequiredMixin, UpdateView):
    model = Distribution
    fields = ('name', 'start_datetime', 'end_datetime', 'frequency', 'message_id')
    success_url = reverse_lazy('distribution:distribution_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.save()

        return super().form_valid(form)


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

class DistributionDeleteView(DeleteView):
    model = Distribution
    success_url = reverse_lazy('distribution:distribution_list')
