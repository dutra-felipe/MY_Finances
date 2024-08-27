from django.urls import path
from . import views


urlpatterns = [
    path('type/list/', views.OperationTypeListView.as_view(), name='type_list'),
    path('type/create/', views.OperationTypeCreateView.as_view(), name='type_create'),
    path('type/<int:pk>/detail/', views.OperationTypeDetailView.as_view(), name='type_detail'),
    path('type/<int:pk>/update/', views.OperationTypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', views.OperationTypeDeleteView.as_view(), name='type_delete'),

]
