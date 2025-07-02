from django.core.management.base import BaseCommand, CommandError

from esi_client.api.market_api import MarketApi
from esi_client.api.universe_api import UniverseApi

from apps.esi.utils import load_type_from_esi
from apps.esi.models.market import MarketGroup, MarketGroupType
from apps.esi.models.type import Type


class Command(BaseCommand):
    help = 'Load Market groups'

    def handle(self, *args, **options):
        mkt = MarketApi()
        uni = UniverseApi()

        # Truncate
        MarketGroup.objects.all().delete()

        total = 0

        esi_groups = mkt.get_markets_groups()
        for mg in esi_groups:
            esi_mkt_group = mkt.get_markets_groups_market_group_id(mg)

            mkt_group, _ = MarketGroup.objects.get_or_create(
                market_group_id=mg
            )
            mkt_group.description = esi_mkt_group.description
            mkt_group.name = esi_mkt_group.name
            mkt_group.parent_group_id = esi_mkt_group.parent_group_id if 'parent_group_id' in esi_mkt_group else 0
            mkt_group.save()

            for t in esi_mkt_group.types:
                type, created = Type.objects.get_or_create(
                    type_id = t
                )
                if created:
                    esi_type = uni.get_universe_types_type_id(t)
                    load_type_from_esi(t)

                mkt_group_type, _ = MarketGroupType.objects.get_or_create(
                    market_group=mkt_group,
                    type=type
                )

        self.stdout.write(
            self.style.SUCCESS('Done')
        )
