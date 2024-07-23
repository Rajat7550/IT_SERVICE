from django.urls import path

from apps.service.views import CreateServiceView, ListServiceView, ListServiceViewJson, UpdateServiceView, \
    DeleteServiceView

urlpatterns = [
    path('admin/service/add', CreateServiceView.as_view(), name='admin-service-add'),
    path('admin/service/list', ListServiceView.as_view(), name='admin-service-list'),
    path('admin/service/list/ajax', ListServiceViewJson.as_view(), name='admin-service-list-ajax'),
    path('admin/service/edit/<int:pk>', UpdateServiceView.as_view(), name='admin-service-edit'),
    path('admin/service/delete/<int:pk>', DeleteServiceView.as_view(), name='admin-service-delete'),
]