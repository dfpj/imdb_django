# Generated by Django 4.0.2 on 2022-02-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]