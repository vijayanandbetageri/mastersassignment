# Generated by Django 3.2.5 on 2021-09-20 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_subcategory_categoryrel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='categoryrel',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
