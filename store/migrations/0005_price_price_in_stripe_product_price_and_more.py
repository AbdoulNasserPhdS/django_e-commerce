# Generated by Django 4.2 on 2023-04-28 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_price_product_stripe_product_id_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='price_in_stripe',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='store.product'),
        ),
    ]
