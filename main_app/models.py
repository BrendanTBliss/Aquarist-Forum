from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# # Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=600)
    image = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            # return f"Posted: {self.post_date} - Post Title: {self.title} - Author: {self.user.first_name}, posted an article about {self.city.name}."
            return f"{self.title}"    
    class Meta:
        ordering = ['post_date']
