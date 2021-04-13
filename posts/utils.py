import os
from django.conf import settings
import datetime

def blog_directory_path(instance, filename):
    
    date_fields = str(datetime.date.today()).split('-')
    year = date_fields[0]
    month = date_fields[1]
    day = date_fields[2]

    # file will be uploaded to MEDIA_ROOT/blog/YEAR/MONTH/DAY//_<produit_id>_<filename>
    blog_sub_path = 'produits/{0}/{1}/{2}/blog/{3}/image_{4}'.format(year, month, day,instance.id, filename)
    blog_full_path = os.path.join(settings.MEDIA_ROOT, blog_sub_path)
    if os.path.exists(blog_full_path):
        os.remove(blog_full_path)
    return blog_sub_path
