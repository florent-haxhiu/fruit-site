# Generated by Django 4.0.5 on 2022-07-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='fruit',
            name='type',
        ),
    ]