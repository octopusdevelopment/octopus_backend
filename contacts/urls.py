from .views import contact, ask_membership, ask_demo
from django.urls import path 

urlpatterns = [
    path('contacter/', contact, name='send message'),
    path('demander-abonnement/', ask_membership, name='ask membership'),
    path('demander-demo/', ask_demo, name='ask demo')
]