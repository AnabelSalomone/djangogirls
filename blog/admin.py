from django.contrib import admin
from .models import Post # we include the Post model

admin.site.register(Post) # so the model is visible in the admin page