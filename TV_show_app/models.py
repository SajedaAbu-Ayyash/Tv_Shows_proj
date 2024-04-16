from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Title must be at least 3 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network shoud be at least 3 characters."
        if len(postData['description']) < 10:
            errors['description'] = "Description must be at least 10 characters."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = ShowManager()


def display_shows():
    return Show.objects.all()
# Create your models here.
