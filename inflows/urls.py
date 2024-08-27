from django.urls import path
from . import views


urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflows_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflows_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflows_detail'),
    path('inflows/<int:pk>/delete/', views.InflowDeleteView.as_view(), name='inflows_delete'),
]
