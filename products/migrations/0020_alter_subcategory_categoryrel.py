# Generated by Django 3.2.5 on 2021-09-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20210920_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='categoryrel',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
