# Generated by Django 4.2 on 2023-06-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_siteinfo_dribble_alter_siteinfo_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='dribble',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='facebook',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='instagram',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='pintarest',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='twitter',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='website_link',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
