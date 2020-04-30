from datetime import datetime, timedelta

from django.db.models import Q
from django.template.loader import render_to_string

from .models import Sentence

def get_contacts_permission(user_1, user_2):
    q_1 = Q(who_offers=user_1, whomever_is_offered=user_2)
    q_2 = Q(who_offers=user_2, whomever_is_offered=user_1)
    q = q_1 | q_2
    time = datetime.today() - timedelta(days=7)
    return Sentence.objects.filter(q, permission=True, updated_at__gte=time).exists()


def offer_email(instance):
    subject = render_to_string('sentence/email/subject.txt', {'user': instance.who_offers})
    context = {
        'user': instance.who_offers,
        'message': instance.message_1,
        'books': instance.books_of_interest_1.all(),
    }
    email_body = render_to_string('sentence/email/email_body_for_proposed.txt', context)

    instance.whomever_is_offered.email_user(subject, email_body, fail_silently=True)

def response_to_offer_email(instance):
    if instance.permission:
        subject = render_to_string('sentence/email/subject_response.txt', {'user': instance.whomever_is_offered})
        context = {
            'user': instance.whomever_is_offered,
            'books': instance.books_of_interest_2.all(),
        }
        email_body = render_to_string('sentence/email/confirmation_email.txt', context)
        instance.who_offers.email_user(subject, email_body, fail_silently=True) 

    elif instance.permission == False:
        subject = render_to_string('sentence/email/subject_response.txt', {'user': instance.whomever_is_offered})
        context = {
            'user': instance.whomever_is_offered,
            'message': instance.reason_for_refusal,
        }
        email_body = render_to_string('sentence/email/renouncement_email.txt', context)

        instance.who_offers.email_user(subject, email_body, fail_silently=True)