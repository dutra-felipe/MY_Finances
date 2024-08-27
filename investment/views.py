from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from type.models import Type
from investment.utils import get_stock_info


class InvestmentListView(ListView):
    model = models.Investment
    template_name = 'investment_list.html'
    context_object_name = 'investments'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        investment_type = self.request.GET.get('investment_type')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if investment_type:
            queryset = queryset.filter(investment_type__id=investment_type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = Type.objects.all()
        return context


class InvestmentCreateView(CreateView):
    model = models.Investment
    template_name = 'investment_create.html'
    form_class = forms.InvestmentForm
    success_url = reverse_lazy('investments_list')


class InvestmentDetailView(DetailView):
    model = models.Investment
    template_name = 'investment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        investment = self.object
        stock_info = get_stock_info(investment.symbol)
        context['stock_info'] = stock_info
        return context


class InvestmentUpdateView(UpdateView):
    model = models.Investment
    template_name = 'investment_update.html'
    form_class = forms.InvestmentForm
    success_url = reverse_lazy('investments_list')


class InvestmentDeleteView(DeleteView):
    model = models.Investment
    template_name = 'investment_delete.html'
    success_url = reverse_lazy('investments_list')
