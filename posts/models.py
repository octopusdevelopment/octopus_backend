from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Post category
class Category(models.Model):
    
    name = models.CharField(verbose_name="Nom Catégorie", max_length=200, db_index=True)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("posts:post-by-category", args = [self.slug])


# Post sub category 
class SubCategory(models.Model):
    name = models.CharField(verbose_name="Sous Catégorie", max_length=200, db_index=True)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Catégorie', related_name="sub_categories")
    class Meta:
        ordering = ('name',)
        verbose_name = 'Sous Catégorie'
        verbose_name_plural = 'Sous Catégories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("posts:post-by-sub-category", args=[self.slug])


# The post without the images 
class PostInfo(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(show=True)


    title = models.CharField(max_length=250)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name='Sous Catégorie')
    slug = models.SlugField(max_length=200, unique=True)
    show = models.BooleanField(verbose_name='Afficher', default=True)
    created = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    image_thumbnail = models.ImageField(upload_to='images/blog/%Y/%m/%d', blank=True, verbose_name="Photo Principale")
    content = RichTextField(blank=False, null=False)

    # Managers
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager

    class Meta:
        ordering = ('-show',)
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug =  slugify(self.title +' '+str(self.id))
        print(self.slug)
        return super(PostInfo, self).save(*args, **kwargs)

# The post with the images

class PostImage(models.Model):
    post = models.ForeignKey(PostInfo, default=None, on_delete=models.CASCADE, verbose_name="Article")
    images = models.FileField(upload_to ='images/blog/%Y/%m/%d', verbose_name="Images associées")
 
    def __str__(self):
        return self.post.slug