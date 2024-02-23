from django.urls import path
from .views import pessoas_list,pessoa_detail_change_and_delete

urlpatterns = [
    path('',pessoas_list),
    path('<int:pk>/',pessoa_detail_change_and_delete),
]
