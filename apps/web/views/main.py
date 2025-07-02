from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.template import loader

from apps.esi.models.category import Category
from apps.esi.models.market import MarketGroup


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = {
            'market': MarketGroup.objects.filter(parent_group_id=0).order_by('name'),
            'categories': Category.objects.order_by('name')
        }

        return context | content

