import datetime
from random import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from . import models, forms


class ProductListView(generic.ListView):
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"
    model = models.Product_list

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")

class ProductDetailView(generic.DetailView):
    template_name = "catalog/product_detail.html"
    context_object_name = "product_id"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Product_list, id=book_id)
