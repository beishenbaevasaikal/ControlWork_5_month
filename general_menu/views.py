from django.shortcuts import render
from . import models
from django.views import generic

class GeneralMenuView(generic.ListView):
    template_name = 'menu/general_menu.html'
    context_object_name = 'slogan'
    model = models.Slogan
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_url'] = models.VideoYouTube.objects.order_by('-id')
        context['top_product'] = models.TopProduct.objects.order_by('-id')
        return context

