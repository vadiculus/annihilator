# Generated by Django 4.0.2 on 2023-02-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_author_alter_order_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='additional_information',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация'),
        ),
    ]