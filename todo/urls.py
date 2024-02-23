from django.urls import path
from .views import PessoaListAndCreate,PessoaDetailChangeAndDelete

urlpatterns = [
    path('',PessoaListAndCreate.as_view()),
    path('<int:pk>/',PessoaDetailChangeAndDelete.as_view()),
]
