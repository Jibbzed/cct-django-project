from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account

def get_balance(request, account_id):
    account = Account.objects.get(id=account_id)
    return JsonResponse({'name': account.name, 'balance': account.balance})

@csrf_exempt
def set_balance(request, account_id):
    if request.method == 'POST':
        balance = request.POST.get('balance')
        account = Account.objects.get(id=account_id)
        account.balance = balance
        account.save()
        return JsonResponse({'status': 'success'})
    return HttpResponse(status=405)

def health_check(request):
    return HttpResponse('OK')