from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.template import loader


from apps.esi.models.category import Category
from apps.esi.models.group import Group


class CategoryView(ListView):
    template_name = 'category.html'
    model = Group
    category = None

    def dispatch(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category_id')
        self.category = Category.objects.get(category_id=category_id)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Group.objects.filter(category=self.category).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = {
            'category': self.category
        }

        return context | content

