from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    zipcode = models.CharField(max_length=30, null=True, blank=True)
    photo = models.ImageField(
        upload_to='profile', default='profile.png')
    address = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def delete(self,*args, **kwargs) :
        self.photo.delete()
        return super().delete(*args, **kwargs)

    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def creat_post_save_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
       
