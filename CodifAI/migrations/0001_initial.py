# Generated by Django 4.0.1 on 2022-06-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('p1', models.BooleanField()),
                ('p2', models.BooleanField()),
                ('p3', models.BooleanField()),
                ('p4', models.BooleanField()),
                ('p5', models.BooleanField()),
                ('p6', models.BooleanField()),
                ('p7', models.BooleanField()),
                ('p8', models.BooleanField()),
                ('p9', models.BooleanField()),
                ('p10', models.BooleanField()),
                ('p11', models.BooleanField()),
                ('lvl0', models.BooleanField()),
                ('lvl1', models.BooleanField()),
                ('lvl2', models.BooleanField()),
                ('lvl3', models.BooleanField()),
                ('percent1', models.FloatField()),
                ('percent2', models.FloatField()),
                ('percent3', models.FloatField()),
            ],
        ),
    ]
