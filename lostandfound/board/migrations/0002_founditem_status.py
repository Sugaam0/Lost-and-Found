# Generated by Django 5.2 on 2025-05-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='status',
            field=models.CharField(choices=[('lost', 'Lost'), ('found', 'Found')], default='found', max_length=10),
            preserve_default=False,
        ),
    ]
