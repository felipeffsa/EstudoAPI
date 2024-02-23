from django.shortcuts import render
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import generics



class PessoaListAndCreate(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
     
        
class PessoaDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


