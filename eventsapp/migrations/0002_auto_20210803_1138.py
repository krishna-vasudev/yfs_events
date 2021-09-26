# Generated by Django 3.2.3 on 2021-08-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='img2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='img3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='img4',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='img5',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='phone_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]