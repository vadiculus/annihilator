# Generated by Django 4.0.2 on 2023-02-22 14:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_product_condition_product_sale_type_alter_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6d17ced5-cdc9-4dfd-b84f-b866a830c056'), editable=False, primary_key=True, serialize=False),
        ),
    ]