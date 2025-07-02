from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView, DetailView
from django.template import loader

from esi_client.api.universe_api import UniverseApi
from esi_client.api.dogma_api import DogmaApi

from apps.esi.utils import load_type_from_esi
from apps.esi.models.category import Category
from apps.esi.models.group import Group
from apps.esi.models.type import Type, TypeAttribute
from apps.esi.models.attribute import Attribute


class TypeView(DetailView):
    template_name = 'type.html'
    model = Type
    category = None
    group = None

    def dispatch(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category_id')
        group_id = self.kwargs.get('group_id')
        self.category = Category.objects.get(category_id=category_id)
        self.group = Group.objects.get(group_id=group_id)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        type_id = self.kwargs.get('type_id')
        return Type.objects.get(type_id=type_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.get_object().name:
            load_type_from_esi(self.get_object().type_id)

        content = {
            'category': self.category,
            'group': self.group
        }

        return context | content
