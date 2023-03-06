# Generated by Django 3.2.18 on 2023-03-05 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('back-end', 'back-end'), ('front-end', 'front-end'), ('IOS', 'IOS'), ('Android', 'Android')], max_length=300)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]