from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, DetailView, ListView

from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'


class ClientProfileView(DetailView):
    template_name = 'webmarket/client_profile.html'
    context_object_name = 'client'

    def get_object(self, queryset=None):
        obj = ClientProfile.objects.first()
        return obj


class PilotProfileView(DetailView):
    template_name = 'webmarket/pilot_profile.html'
    context_object_name = 'pilot'

    def get_object(self, queryset=None):
        obj = PilotProfile.objects.first()
        return obj


class PilotsCatalogueView(ListView):
    template_name = 'webmarket/pilots_catalogue.html'
    context_object_name = 'pilots'

    def get_queryset(self):
        qs = PilotProfile.objects.all()
        return qs


class OrderView(DetailView):
    template_name = 'webmarket/order_detail.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        obj = Order.objects.first()
        return obj


class OrdersCatalogueView(ListView):
    template_name = 'webmarket/orders_catalogue.html'
    context_object_name = 'orders'

    def get_queryset(self):
        qs = Order.objects.all()
        return qs





