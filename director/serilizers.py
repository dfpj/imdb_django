from rest_framework import serializers
from .models import Director

class DirectorSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields =('name','bio','image','id')