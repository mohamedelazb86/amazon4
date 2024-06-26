# Generated by Django 4.2 on 2024-05-07 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=120)),
                ('address_type', models.TextField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Others', 'Others')], max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
