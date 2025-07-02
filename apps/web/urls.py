from django.urls import path

from .views.main import Home
from .views.category import CategoryView
from .views.group import GroupView
from .views.type import TypeView


app_name = 'web'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<int:category_id>', CategoryView.as_view(), name='category'),
    path('<int:category_id>/<int:group_id>', GroupView.as_view(), name='group'),
    path('<int:category_id>/<int:group_id>/<int:type_id>', TypeView.as_view(), name='type'),
]
