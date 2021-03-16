from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#auto_now=True - modify datetime when updating db entry - use in updated_at etc
#auto_now_add=True - can't modify , add date only when entry is created
# to check created migration run :  py manage.py sqlmigrate blog 0001 (<- app name, migration number)
# to access all posts of a user : user.post_set.all() <- add _set to post variable
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #  create get_absolute_url to avoid redirect errors for created/updated posts for non-default route names
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # reverse to created post