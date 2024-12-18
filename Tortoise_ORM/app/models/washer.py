from tortoise import fields
from tortoise.models import Model


class Washer(Model):
    washer_id = fields.IntField(pk=True, index=True)
    name= fields.CharField(max_length=250)
    diameter = fields.FloatField()
    weight = fields.FloatField()
    accuracy_class = fields.CharField(max_length=1)
    strength_class = fields.FloatField()
    cost = fields.FloatField()

    class Meta:
        table = 'washers'
    
    def __str__(self):
        return f'{self.name} {self.diameter}'
