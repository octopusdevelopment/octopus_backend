from django.db import models

class GeneralContact(models.Model):

    fullName = models.CharField(verbose_name='Nom complet', max_length=100)
    email = models.EmailField(verbose_name="Email", null=True, blank = True)
    phone = models.CharField(verbose_name="Téléphone" , max_length=25)
    subject = models.CharField(verbose_name="Sujet", max_length=50, blank=False)
    message = models.TextField(verbose_name="Message", blank=False, null=False)
    date_sent = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    treated = models.BooleanField(verbose_name="Traité", default=False)
   
    class Meta:
        ordering = ('-date_sent',)
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.subject


class SubScription_Category(models.Model):
    name = models.CharField(verbose_name='Type Abonnement', max_length=100)
    price =  models.DecimalField(verbose_name='Prix Mensuel',  max_digits=10, decimal_places=2, default=2000)
    
    class Meta:
            ordering = ('-name',)
            verbose_name = "Catégorie"
            verbose_name_plural = "Catégories"
    
    def __str__(self):
        return self.name

class Subscription(models.Model):
    category = models.ForeignKey(SubScription_Category, on_delete= models.PROTECT, related_name="subscriptions" ,verbose_name='Catégorie', default='basic')
    fullName = models.CharField(verbose_name='Nom complet', max_length=100)
    email = models.EmailField(verbose_name="Email", null=True, blank = True)
    phone = models.CharField(verbose_name="Téléphone" , max_length=25, blank=False, null=False)
    description =  models.TextField(verbose_name='Description')
    date_start = models.DateTimeField(verbose_name="Date Début", auto_now_add=True)
    date_end = models.DateTimeField(verbose_name="Date de Fin", auto_now_add=True)

    class Meta:
            ordering = ('date_start',)
            verbose_name = "Abonnement"
            verbose_name_plural = "Abonnements"

    def __str__(self):
        return str(self.id)


class Demo(models.Model):
    category = models.ForeignKey(SubScription_Category, on_delete= models.PROTECT, related_name="trials" ,verbose_name='Catégorie', default='basic')
    fullName = models.CharField(verbose_name='Nom complet', max_length=100)
    email = models.EmailField(verbose_name="Email", null=True, blank = True)
    phone = models.CharField(verbose_name="Téléphone" , max_length=25, blank=False, null=False)
    description =  models.TextField(verbose_name='Description')
    date_start = models.DateTimeField(verbose_name="Date Début", auto_now_add=True)
    date_end = models.DateTimeField(verbose_name="Date de Fin", auto_now_add=True)

    class Meta:
            ordering = ('date_start',)
            verbose_name = "Demande Démo"
            verbose_name_plural = "Demandes démo"

    def __str__(self):
        return str(self.id)