from django.urls import path
from . import views
from .views import update_dividends


urlpatterns = [
    path('dividend/list/', views.DividendListView.as_view(), name='dividend_list'),
    path('dividend/<int:pk>/detail/', views.DividendDetailView.as_view(), name='dividend_detail'),
    path('dividend/update/', update_dividends, name='dividend_update'),

]
