# Generated by Django 4.0 on 2024-04-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totine_of_app', '0007_alter_groupetontinee_date_decréation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupetontinee',
            name='date_decréation',
            field=models.DateTimeField(),
        ),
    ]
