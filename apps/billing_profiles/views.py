from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .models import BillingProfile

# Create your views here.

class BillingProfileListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'billing_profiles/billing_profiles.html'

    def get_queryset(self):
        return self.request.user.billing_profiles

@login_required(login_url='login')
def create(request):

    if request.method == 'POST':
        if request.POST.get('stripeToken'):
            if not request.user.has_customer():
                request.user.create_customer_id()
            stripe_token = request.POST.get('stripeToken')
            billing_profile = BillingProfile.objects.create_by_stripe_token(request.user, stripe_token)

            if billing_profile:
                messages.success(request, 'Tarjeta creada exitosamente' )
    return render(request, 'billing_profiles/create.html', {
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })

@login_required(login_url='login')
def default(request, pk):
    billing_profile =  get_object_or_404(BillingProfile, pk=pk)

    if request.user.id != billing_profile.user.id:
        return redirect('billing_profiles:billing_profiles')
    
    if request.user.has_billing_profile():
        request.user.billing_profile.update_default()
    
    billing_profile.update_default(True)

    return redirect('billing_profiles:billing_profiles')

@login_required(login_url='login')
def delete(request, pk):
    billing_profile =  get_object_or_404(BillingProfile, pk=pk)

    if request.user.id != billing_profile.user.id or request.user.billing_profile == billing_profile:
        return redirect('billing_profiles:billing_profiles')
    
    billing_profile.delete_card(request.user)
    return redirect('billing_profiles:billing_profiles')