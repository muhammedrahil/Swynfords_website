# Generated by Django 4.0.4 on 2023-03-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_visted_site_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visted_site',
            name='domain',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]