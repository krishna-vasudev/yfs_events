# Generated by Django 3.2.3 on 2021-10-23 14:35

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('uploaded_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('blog_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader', models.CharField(max_length=200)),
                ('parent_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader', models.CharField(max_length=200)),
                ('commented_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', models.TextField(blank=True)),
                ('parent_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
