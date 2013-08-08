"""
Beging porting from django-stripe-payments
"""
from payments import settings


def payments_settings(request):
    # TODO - needs tests
    return {
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        "PLAN_CHOICES": settings.PLAN_CHOICES,  # possibly nuke
        "PAYMENT_PLANS": settings.PAYMENTS_PLANS  # possibly nuke
    }