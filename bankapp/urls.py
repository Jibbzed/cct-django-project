from django.urls import path
from .views import get_balance, set_balance, health_check

urlpatterns = [
    path('account/<int:account_id>/balance/', get_balance),
    path('account/<int:account_id>/set_balance/', set_balance),
    path('health/', health_check),
]