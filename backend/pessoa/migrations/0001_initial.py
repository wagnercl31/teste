# Generated by Django 3.0.3 on 2020-03-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
