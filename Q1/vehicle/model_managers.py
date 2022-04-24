from django.db import models
from datetime import timedelta
from django.utils import timezone


class NavigationRecordManager(models.Manager):

    def get_last_records(self):

        start_date = timezone.now() - timedelta(days=2)
        return super().get_queryset().select_related() \
                                .filter(datetime__gte=start_date) \
                                .order_by("vehicle", "-datetime") \
                                .distinct("vehicle")