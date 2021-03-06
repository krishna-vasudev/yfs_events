# Generated by Django 3.2.3 on 2021-07-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('venue', models.TextField()),
                ('event_description', models.TextField()),
                ('organizer_name', models.CharField(max_length=60)),
                ('phone_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('event_activity', models.BooleanField()),
                ('event_registration', models.BooleanField()),
                ('reg_link', models.TextField()),
                ('img1', models.ImageField(upload_to='images/')),
                ('img2', models.ImageField(upload_to='images/')),
                ('img3', models.ImageField(upload_to='images/')),
                ('img4', models.ImageField(upload_to='images/')),
                ('img5', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
