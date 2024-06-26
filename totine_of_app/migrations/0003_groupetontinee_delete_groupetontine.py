# Generated by Django 4.0 on 2024-04-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totine_of_app', '0002_rolee'),
    ]

    operations = [
        migrations.CreateModel(
            name='groupetontinee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('cotisation_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frequence_despaiement', models.CharField(max_length=50)),
                ('date_decréation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='groupetontine',
        ),
    ]
