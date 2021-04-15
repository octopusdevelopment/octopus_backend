from django.core.mail import EmailMessage
from django.conf import settings


def send_email(subject, fullName, phone, email, message, type_message):
    subject = f'Octopus - {subject}'

    message = f'Vous venez de recevoir un nouveau message de la part de: {fullName},\n' \
              f'Email: {email},\n' \
              f'Numéro de téléphone: {phone},\n' \
              f'Type: {type_message},\n' \
              f'Message: {message}'


  
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['hello@octopus-consulting.com', 'commercial@octopus-consulting.com', 'Hildweig@gmail.com'])

    email.send()

    return True;