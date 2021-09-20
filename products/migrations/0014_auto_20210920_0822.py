# Generated by Django 3.2.5 on 2021-09-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_subcategory_categoryrel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='categoryrel',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
