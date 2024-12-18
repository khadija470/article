# Generated by Django 5.1.1 on 2024-10-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image_alter_article_date_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='disponible',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='mode_conservation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='origine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='prix_kilo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='quantite_disponible',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='temps_livraison',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
