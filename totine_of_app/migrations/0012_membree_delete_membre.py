# Generated by Django 4.0 on 2024-04-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totine_of_app', '0011_alter_groupetontinee_date_decréation'),
    ]

    operations = [
        migrations.CreateModel(
            name='membree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_groupe', models.CharField(max_length=150)),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=10)),
                ('numero_telephon', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='membre',
        ),
    ]
