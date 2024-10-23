# Generated by Django 5.1.1 on 2024-10-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_publication',
            field=models.DateField(auto_now_add=True),
        ),
    ]