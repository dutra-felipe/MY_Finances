from django.views.generic import ListView, CreateView, DetailView, DeleteView
from . import models, forms
from django.urls import reverse_lazy


class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        asset = self.request.GET.get('asset')

        if asset:
            queryset = queryset.filter(asset__name__icontains=asset)

        return queryset


class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflows_list')


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'


class OutflowDeleteView(DeleteView):
    model = models.Outflow
    template_name = 'outflow_delete.html'
    success_url = reverse_lazy('outflows_list')
