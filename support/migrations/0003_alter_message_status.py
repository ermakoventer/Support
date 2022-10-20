# Generated by Django 4.1.2 on 2022-10-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_delete_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('FR', 'Frozen'), ('RD', 'Resolved'), ('URD', 'Unresolved')], default='FR', max_length=10),
        ),
    ]