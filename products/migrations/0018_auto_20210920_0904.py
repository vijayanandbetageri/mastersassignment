# Generated by Django 3.2.5 on 2021-09-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_subcategory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='category',
            new_name='categoryrel',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='categoryrel',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
