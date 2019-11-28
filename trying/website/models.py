from django.db import models

# Create your models here.
class Roast(models.Model):
    roast_text=models.CharField(max_length=10000)
    pub_date=models.DateTimeField('date published')
    votes=models.IntegerField(default=0)