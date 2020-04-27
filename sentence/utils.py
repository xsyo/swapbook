from datetime import datetime, timedelta

from django.db.models import Q

from .models import Sentence

def get_contacts_permission(user_1, user_2):
    q_1 = Q(who_offers=user_1, whomever_is_offered=user_2)
    q_2 = Q(who_offers=user_2, whomever_is_offered=user_1)
    q = q_1 | q_2
    time = datetime.today() - timedelta(days=7)
    return Sentence.objects.filter(q, permission=True, updated_at__gte=time).exists()

