# Generated by Django 3.2.5 on 2021-09-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210920_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='categoryrel',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]