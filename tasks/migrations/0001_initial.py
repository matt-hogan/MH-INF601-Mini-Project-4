# Generated by Django 4.1.3 on 2022-11-06 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required', max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
