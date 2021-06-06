# Generated by Django 3.2 on 2021-06-06 11:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale_item',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='sale_item',
            name='sold_at',
        ),
        migrations.RemoveField(
            model_name='stock_item',
            name='added_at',
        ),
        migrations.AddField(
            model_name='sale_total',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.customer'),
        ),
        migrations.AddField(
            model_name='sale_total',
            name='sold_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock_total',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
