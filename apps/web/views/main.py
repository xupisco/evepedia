from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.template import loader


from apps.esi.models.category import Category


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = {
            'categories': Category.objects.order_by('name')
        }

        return context | content

