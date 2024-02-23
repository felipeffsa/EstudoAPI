from django.shortcuts import render
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound




class PessoaListAndCreate(APIView):
    def get(self,request):
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PessoaSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        
class PessoaDetailChangeAndDelete(APIView):
    def get_object(self, pk):
        try:
           return Pessoa.objects.get(pk = pk)
        except Pessoa.DoesNotExist:
            raise NotFound()
    def get(self,request, pk):
        pessoa = self.get_object(pk)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)
    def put(self,request, pk):
        pessoa = self.get_object(pk)
        serializer = PessoaSerializer(pessoa, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self, request, pk):
        pessoa = self.get_object(pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

