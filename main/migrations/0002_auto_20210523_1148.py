# Generated by Django 3.1.7 on 2021-05-23 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.flights'),
        ),
    ]