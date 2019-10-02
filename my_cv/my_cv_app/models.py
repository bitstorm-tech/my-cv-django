from django.db import models


class ValueItem(models.Model):
    business_id = models.TextField()
    name = models.TextField()
    level = models.IntegerField()
    children = models.ManyToManyField(to='ValueItem')

    def __str__(self):
        return f"business_id='{self.business_id}', name='{self.name}', level={self.level}"
