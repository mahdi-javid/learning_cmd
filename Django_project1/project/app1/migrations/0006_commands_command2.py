# Generated by Django 2.2.5 on 2019-10-30 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20191029_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='commands',
            name='command2',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
