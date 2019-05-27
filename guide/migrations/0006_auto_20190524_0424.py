# Generated by Django 2.2.1 on 2019-05-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_auto_20190523_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='siteurl',
            field=models.URLField(null=True),
        ),
    ]
