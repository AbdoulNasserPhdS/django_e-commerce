# Generated by Django 4.2 on 2023-05-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default.jpg', null=True, upload_to='products'),
        ),
    ]
