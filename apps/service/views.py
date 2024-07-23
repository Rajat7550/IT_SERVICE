from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.service.forms import CreateServiceForm
from apps.service.models import Service


# Create your views here.



class CreateServiceView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Service
    form_class = CreateServiceForm
    template_name = 'admin/service/form.html'
    success_message = "Service created successfully"
    success_url = reverse_lazy('admin-service-list')


class UpdateServiceView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Service
    form_class = CreateServiceForm
    template_name = 'admin/service/form.html'
    success_message = "Service updated successfully"
    success_url = reverse_lazy('admin-service-list')



class ListServiceView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/service/list.html'


class ListServiceViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Service
    columns = ['service_name','payment_terms','service_package','service_price','service_tax','service_image','active','actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.filter(active=True)

    def render_column(self, row, column):
        if column == 'active':
            if row.active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'

        if column=='service_image':
            return f'<img src="{row.service_image.url}"  width="100px" >'

        if column == 'actions':
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-service-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-service-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        else:
            return super(ListServiceViewJson, self).render_column(row, column)

class DeleteServiceView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Service

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)
