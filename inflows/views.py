from django.views.generic import ListView, CreateView, DetailView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from .utils import get_stock_price_on_date, calculate_portfolio_valorization
import yfinance as yf


class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        asset = self.request.GET.get('asset')

        if asset:
            queryset = queryset.filter(asset__name__icontains=asset)

        return queryset


class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflows_list')


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inflow = self.get_object()

        symbol = inflow.asset.symbol
        purchase_date = inflow.created_at.strftime('%Y-%m-%d')

        # Preço no dia da compra
        stock_price_on_date = round(get_stock_price_on_date(symbol, purchase_date), 4)

        # Preço atual
        current_price = yf.Ticker(symbol).info['currentPrice']

        # Calcular valorização considerando múltiplas compras
        total_quantity = inflow.asset.quantity
        total_amount = inflow.asset.amount

        # Preço médio
        average_price = float(total_amount / total_quantity)

        # Valorização
        valorization = round(((current_price - average_price) / average_price) * 100, 4)

        # Calcular valorização total da carteira
        inflows = models.Inflow.objects.all()
        total_portfolio_valorization = calculate_portfolio_valorization(inflows)

        context['stock_info'] = {
            'date': stock_price_on_date,
            'currentPrice': current_price,
            'averageprice': average_price,
            'valorization': valorization,
        }

        context['total_portfolio_valorization'] = total_portfolio_valorization

        return context


class InflowDeleteView(DeleteView):
    model = models.Inflow
    template_name = 'inflow_delete.html'
    success_url = reverse_lazy('inflows_list')
