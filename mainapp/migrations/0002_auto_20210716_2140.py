# Generated by Django 3.2.5 on 2021-07-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='owner_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='importer',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='importer',
            name='owner_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='importer',
            name='phone_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_stock',
            field=models.BooleanField(default=True),
        ),
    ]