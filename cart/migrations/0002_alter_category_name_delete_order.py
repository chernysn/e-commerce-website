# Generated by Django 4.2.6 on 2023-10-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]