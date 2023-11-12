from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    iscompleted = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
