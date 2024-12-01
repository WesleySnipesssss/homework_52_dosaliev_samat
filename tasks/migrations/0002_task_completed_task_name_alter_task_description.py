# Generated by Django 5.1.3 on 2024-12-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='Unnamed Task', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
