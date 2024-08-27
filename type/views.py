from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy


class OperationTypeListView(ListView):
    model = models.Type
    template_name = 'type_list.html'
    context_object_name = 'types'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class OperationTypeCreateView(CreateView):
    model = models.Type
    template_name = 'type_create.html'
    form_class = forms.TypeForm
    success_url = reverse_lazy('type_list')


class OperationTypeDetailView(DetailView):
    model = models.Type
    template_name = 'type_detail.html'


class OperationTypeUpdateView(UpdateView):
    model = models.Type
    template_name = 'type_update.html'
    form_class = forms.TypeForm
    success_url = reverse_lazy('type_list')


class OperationTypeDeleteView(DeleteView):
    model = models.Type
    template_name = 'type_delete.html'
    success_url = reverse_lazy('type_list')
