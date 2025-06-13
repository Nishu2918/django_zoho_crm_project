from django.urls import path
from .views import display_leads_view, fetch_leads_view, zoho_webhook_listener

urlpatterns = [
    path('', display_leads_view, name='display_leads'),
    path('fetch/', fetch_leads_view, name='fetch_leads'),
    path('webhook/', zoho_webhook_listener, name='zoho_webhook'),
]
