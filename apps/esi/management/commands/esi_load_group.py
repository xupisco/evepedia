from django.core.management.base import BaseCommand, CommandError

from esi_client.api.universe_api import UniverseApi

from apps.esi.models.category import Category
from apps.esi.models.group import Group
from apps.esi.models.type import Type


class Command(BaseCommand):
    help = 'Load group data by ID (required)'

    def add_arguments(self, parser):
        parser.add_argument('group_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        uni = UniverseApi()
        total = 0
        group_ids = options['group_ids']

        for g in group_ids:
            esi_group = uni.get_universe_groups_group_id(g)
            category = Category.objects.get(category_id=esi_group.category_id)

            group = Group.objects.get(group_id=esi_group.group_id)
            group.name = esi_group.name
            group.published = esi_group.published
            group.save()

            for t in esi_group.types:
                type, _ = Type.objects.get_or_create(
                    group=group,
                    type_id=t
                )

        self.stdout.write(
            self.style.SUCCESS('Done')
        )
