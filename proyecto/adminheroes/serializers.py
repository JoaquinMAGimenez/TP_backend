from rest_framework import serializers

from adminheroes.models import Superheroe, Universo


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superheroe
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'

class UniversoSerealizar (serializers.ModelSerializer):
    class Meta:
        model = UniversoSerealizar
        fields = '__all__'