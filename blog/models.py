from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # limited character textfield
    text = models.TextField() # no limit textfield
    created_date = models.DateTimeField(
            default=timezone.now) # date and time field
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now() # establishes the date and time when the post is sent
        self.save() # saves it to the database

    def __str__(self):
        return self.title