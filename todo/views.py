from django.shortcuts import render
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def pessoas_list(request):
    if request.method =='GET':
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = PessoaSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def pessoa_detail_change_and_delete(request, pk):
    try:
        pessoa = Pessoa.objects.get(pk = pk)
    except Pessoa.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = PessoaSerializer(pessoa, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)