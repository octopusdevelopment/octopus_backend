# Generated by Django 3.0.7 on 2021-05-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(upload_to='services'),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='icon_url',
            field=models.ImageField(upload_to='service_categories'),
        ),
    ]