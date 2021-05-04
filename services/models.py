from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# service category
class ServiceCategory(models.Model):
    
    name = models.CharField(verbose_name="Nom Catégorie", max_length=200)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    description = models.CharField(max_length=400)

    icon= models.ImageField(upload_to='service_categories', verbose_name = 'Icon')
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def save(self, *args, **kwargs):
        self.slug =  slugify(self.name)
        return super(ServiceCategory, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


# The service without the images 
class Service(models.Model):

    class serviceObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(show=True)


    title = models.CharField(max_length=250, verbose_name='Titre')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=400, verbose_name= 'Description')

    category = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, verbose_name='Catégorie')
    icon = models.FileField(upload_to='services', verbose_name='Icon bleue')
    icon_white = models.FileField(upload_to='services', verbose_name = 'Icon Blanche', default='icon')
    show = models.BooleanField(verbose_name='Afficher', default=True)
    show_home = models.BooleanField(verbose_name='Afficher dans l\'accueil', default=True)
    
    
    # Managers
    objects = models.Manager() # default manager
    serviceobjects = serviceObjects() # custom manager

    class Meta:
        ordering = ('-show',)
        verbose_name = "Service"
        verbose_name_plural = "Services"
        

    def save(self, *args, **kwargs):

        self.slug =  slugify(self.title)
        return super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

# The service with the images

class ServiceContent(models.Model):

    service = models.ForeignKey(Service, default=None, on_delete=models.CASCADE, verbose_name="Service")
    header = models.CharField(max_length=250)
    text = RichTextField(blank=False, null=False, default='text')
    order = models.IntegerField(blank=False, null=False, default=1)

    def __str__(self):
        return self.service.slug

    