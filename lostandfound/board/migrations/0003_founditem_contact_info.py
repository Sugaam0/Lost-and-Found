# Generated by Django 5.2 on 2025-05-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_founditem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='contact_info',
            field=models.CharField(default='found', help_text='Phone number or email', max_length=100),
            preserve_default=False,
        ),
    ]
