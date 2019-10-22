from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Row(models.Model):
    """"""
    num = models.IntegerField(default=0, null=True)
    content = models.CharField(default='123456789', max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        default_permissions = ('add', 'change', 'delete')

    def __str__(self):
        return str(self.num)
