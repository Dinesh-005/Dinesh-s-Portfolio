# Generated by Django 5.0.6 on 2024-05-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
