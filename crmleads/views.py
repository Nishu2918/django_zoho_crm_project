from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
import logging
import json 
from .models import Lead

from .zoho_client import get_zoho_leads

logger = logging.getLogger(__name__)

@require_GET
def fetch_leads_view(request):
    try:
        data = get_zoho_leads()
        return JsonResponse(data, safe=False)
    except Exception as e:
        logger.exception("Failed to fetch Zoho leads")
        return JsonResponse({"error": "Failed to fetch leads."}, status=500)

def display_leads_view(request):
    leads = []
    try:
        leads = get_zoho_leads().get("data", [])
    except Exception as e:
        logger.exception("Error fetching leads for display view")
    return render(request, 'crmleads/display_leads.html', {'leads': leads})

@csrf_exempt
@require_POST
def zoho_webhook_listener(request):
    try:
        data = json.loads(request.body)
        print("Webhook Data:", data)

        # Save data to DB
        Lead.objects.create(
            first_name=data.get("first_name", ""),
            last_name=data.get("lastname", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
            company=data.get("company", ""),
            lead_id=data.get("lead_id", "")
        )

        return JsonResponse({'message': 'Webhook received and lead saved'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)