from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, FormView, DetailView
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Category, Items
from django.views import View
from .forms import ItemForm

from .serializers import CategorySerializer, ItemSerializer, ItemCteateSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import filters

class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'




class MainView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        items = []
        for category in categories:
            if len(items) <= 20:
                items.append(Items.objects.filter(category=category)[:3])
        return render(request, 'main-page.html', {'categories':categories, 'last_items': items})


class CategotyView(DetailView):
    model = Items
    template_name = 'category-page.html'

    def get_context_data(self, **kwargs):
            context = super(CategotyView, self).get_context_data(**kwargs)
            context['categories'] = Category.objects.all()
            context['active_pk'] = int(self.kwargs.get('pk'))
            context['items'] =Items.objects.filter(category__id=self.kwargs.get('pk'))
            return context

class ItemDetail(DetailView):
    model = Items
    fields = ['title']
    template_name = 'item-page.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        item = Items.objects.get(pk=int(self.kwargs.get('pk')))
        context['active_pk'] = item.category_id
        return context


class CreateItem(FormView):
    model = Items
    template_name = 'create-item.html'
    form_class = ItemForm
    success_url = reverse_lazy('main-page')

    def get_context_data(self, **kwargs):
        context = super(CreateItem, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super(CreateItem, self).form_valid(form)




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = 'get'
    # filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    # ordering_fields = ('created', 'updated')
    # filter_fields = ('active', 'id', 'name', 'address_1', 'address_3', 'address_2', 'mobile_number', 'postcode',
    #                  'landline_number', 'facebook', 'twitter', 'website', 'vat_reg_no')



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    http_method_names = 'get'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category',)


class DetailView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    http_method_names = 'get'
    lookup_field = 'id'


class CreateItemView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemCteateSerializer
