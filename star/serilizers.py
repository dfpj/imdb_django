from rest_framework import serializers
from .models import Star

class StarSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields =('name','bio','image','id')