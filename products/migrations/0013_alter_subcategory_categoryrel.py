# Generated by Django 3.2.5 on 2021-09-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210920_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='categoryrel',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
