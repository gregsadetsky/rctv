import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class User(AbstractUser):
    pass


class App(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # creates some stable order that we can use to 'order' apps...
    # TODO have more ability to re-order apps? or always show them randomly?
    created_at = models.DateTimeField(auto_now_add=True)
    # https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers
    url = models.URLField(max_length=1000)

    def __str__(self):
        return f"{self.url}"
