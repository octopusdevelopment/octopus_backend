from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import GeneralContact, Subscription, SubScription_Category, Demo
from django.shortcuts import get_object_or_404

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@require_POST
@csrf_exempt
def contact(request):

    data = json.loads(request.body.decode("utf-8"))['data']

    fullName = data['name']
    email = data['email']
    phone = data['phone']
    subject = data['subject']
    message = data['message']

    success = False
    msg = 'Une erreur est survenue, veuillez réessayer'

    try:
        contact = GeneralContact(fullName=fullName, email=email, phone=phone, subject=subject, message=message)
        contact.save()
        success = True
        msg = 'Votre message a été bien envoyé.'
    except:
        pass
    res = {
        'success': success,
        'message': msg
    }
    return JsonResponse(res)
import traceback

@require_POST
@csrf_exempt
def ask_membership(request):

    data = json.loads(request.body.decode("utf-8"))['data']
    subsc_cat  = data['category']
    category = get_object_or_404(SubScription_Category, name=subsc_cat )
    fullName = data['name']
    email = data['email']
    phone = data['phone']

    try:
        message = data['message']
        print('message', message)
    except:
        message= ''

    success = False
    msg = 'Une erreur est survenue, veuillez réessayer'

    try:
        Subscription.objects.create(category=category, fullName=fullName, email=email, phone=phone, description=message)
        success = True

        msg = 'Votre demande a bien été envoyée.'
    except Exception as e:
        print('shit')
        traceback.print_exc()
        success = False
        msg = 'Une erreur est survenue, veuillez réessayer'
    res = {
        'success': success,
        'message': msg
    }
    return JsonResponse(res)


@require_POST
@csrf_exempt
def ask_demo(request):

    data = json.loads(request.body.decode("utf-8"))['data']
    subsc_cat  = data['category']
   
    category = get_object_or_404(SubScription_Category, name=subsc_cat )
    fullName = data['name']
    email = data['email']
    phone = data['phone']

    try:
        message = data['message']
        print('message', message)
    except:
        message= ''

    success = False
    msg = 'Une erreur est survenue, veuillez réessayer'

    try:
        Demo.objects.create(category=category, fullName=fullName, email=email, phone=phone, description=message)
        success = True

        msg = 'Votre demande a bien été envoyée.'
    except Exception as e:
        print('shit')
        traceback.print_exc()
        success = False
        msg = 'Une erreur est survenue, veuillez réessayer'
    res = {
        'success': success,
        'message': msg
    }
    return JsonResponse(res)
