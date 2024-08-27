from . import models
from .utils import get_stock_dividends
from django.views.generic import ListView, DetailView
from investment.utils import get_stock_info
from investment.models import Investment
from django.shortcuts import redirect
from .models import Dividend


class DividendListView(ListView):
    model = models.Dividend
    template_name = 'dividend_list.html'
    context_object_name = 'dividends'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__name__icontains=name)

        return queryset


class DividendDetailView(DetailView):
    model = models.Dividend
    template_name = 'dividend_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dividend = self.object
        stock_info = get_stock_info(dividend.name.symbol)
        context['stock_info'] = stock_info
        return context


def update_dividends(request):
    dividends = Dividend.objects.all()
    for dividend in dividends:
        investment = Investment.objects.filter(name=dividend.name).first()
        if investment:
            dividends_per_share = get_stock_dividends(dividend.name.symbol)
            total_dividends = dividends_per_share * investment.quantity
            dividend.total_dividends = total_dividends
            dividend.save()

    return redirect('dividend_list')
