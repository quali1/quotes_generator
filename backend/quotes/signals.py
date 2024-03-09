from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Quote


@receiver(m2m_changed, sender=Quote.likes.through)
def update_likes_count(sender, instance, **kwargs):
    instance.likes_count = instance.likes.count()
    instance.save()
