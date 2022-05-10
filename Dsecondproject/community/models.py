from datetime import datetime
from django.db import models
from datetime import datetime
# Create your models here.


class Posting(models.Model):
    country = models.CharField('Country', max_length=20, blank=True)
    plate_name = models.CharField('Plate', max_length=30, blank=True)
    title = models.CharField('Title', max_length=50, blank=True)
    minutes = models.IntegerField('Minutes', blank=True)
    upload_time = models.DateTimeField(default=datetime.now())
    content = models.TextField('Content')

    def __str__(self):
        return self.title
