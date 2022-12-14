# Generated by Django 4.1.3 on 2022-11-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
