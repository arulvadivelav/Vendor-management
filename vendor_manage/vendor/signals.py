from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from vendor.models import PurchaseOrder
from vendor.repository.matrices import update_metrics_repo


@receiver(post_save, sender=PurchaseOrder)
def update_metrics(sender, instance, **kwargs):
    update_metrics_repo(instance)


@receiver(post_delete, sender=PurchaseOrder)
def update_metrics(sender, instance, **kwargs):
    update_metrics_repo(instance)
