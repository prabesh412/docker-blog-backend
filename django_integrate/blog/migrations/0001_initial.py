# Generated by Django 4.0.8 on 2023-03-18 07:07

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
            name='BlogPost',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
