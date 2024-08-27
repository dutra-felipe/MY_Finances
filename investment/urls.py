from django.urls import path
from . import views


urlpatterns = [
    path('investments/list/', views.InvestmentListView.as_view(), name='investments_list'),
    path('investments/create/', views.InvestmentCreateView.as_view(), name='investments_create'),
    path('investments/<int:pk>/detail/', views.InvestmentDetailView.as_view(), name='investments_detail'),
    path('investments/<int:pk>/update/', views.InvestmentUpdateView.as_view(), name='investments_update'),
    path('investments/<int:pk>/delete/', views.InvestmentDeleteView.as_view(), name='investments_delete'),

]
