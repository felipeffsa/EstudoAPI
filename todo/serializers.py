from .models import Pessoa
from rest_framework import serializers

# Create your views here.
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'