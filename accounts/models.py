from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# I create a new model to extend User via OneToOneRelationship
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_ip_used = models.CharField(max_length=32, default=None, null=True, blank=True)
    is_ip_changed = models.BooleanField(default=False, blank=True)


# I intercept each User creation by adding additional Profile information
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# I intercept each User save by updating the additional Profile information
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
