# Generated by Django 4.0.4 on 2022-04-23 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20211229_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='return_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('returned_at', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.customer')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.item')),
            ],
        ),
    ]