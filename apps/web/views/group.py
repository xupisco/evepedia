from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.template import loader


from apps.esi.models.category import Category
from apps.esi.models.group import Group
from apps.esi.models.type import Type


class GroupView(ListView):
    template_name = 'group.html'
    model = Type
    category = None
    group = None

    def dispatch(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category_id')
        group_id = self.kwargs.get('group_id')
        self.category = Category.objects.get(category_id=category_id)
        self.group = Group.objects.get(group_id=group_id)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Type.objects.filter(group=self.group).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = {
            'category': self.category,
            'group': self.group
        }

        return context | content
