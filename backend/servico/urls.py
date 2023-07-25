from django.urls import path

from backend.servico import views as v

app_name = 'servico'

urlpatterns = [
    path('', v.ordem_servico_list, name='ordem_servico_list'),
    path('create/', v.ordem_servico_create, name='ordem_servico_create'),
    path('<int:pk>/', v.ordem_servico_detail, name='ordem_servico_detail'),
    path('<int:pk>/updade', v.ordem_servico_update, name='ordem_servico_update'),
    path('<int:pk>/delete', v.ordem_servico_delete, name='ordem_servico_delete'),
]
