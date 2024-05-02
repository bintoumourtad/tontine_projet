# Generated by Django 4.0 on 2019-01-01 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totine_of_app', '0005_contributions'),
    ]

    operations = [
        migrations.CreateModel(
            name='membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe_tontine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totine_of_app.groupetontinee')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totine_of_app.user')),
            ],
        ),
    ]