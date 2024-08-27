from django.urls import path
from . import views


urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflows_list'),
    path('outflows/create/', views.OutflowCreateView.as_view(), name='outflows_create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflows_detail'),
    path('outflows/<int:pk>/delete/', views.OutflowDeleteView.as_view(), name='outflows_delete'),
]
