# Generated by Django 4.1.3 on 2022-11-14 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_meta_description_product_meta_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='c',
            new_name='category',
        ),
    ]
