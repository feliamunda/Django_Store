from django.urls import path

from . import views

app_name = 'billing_profiles'

urlpatterns = [
    path('', views.BillingProfileListView.as_view(), name='billing_profiles'),
    path('nuevo', views.create, name='create'),
    path('default/<int:pk>', views.default, name='default'),
    path('eliminar/<int:pk>', views.delete, name='delete')
]