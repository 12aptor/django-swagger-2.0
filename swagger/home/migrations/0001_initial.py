# Generated by Django 4.0.4 on 2022-05-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('home_id', models.AutoField(primary_key=True, serialize=False)),
                ('home_nombre', models.CharField(max_length=100)),
            ],
        ),
    ]