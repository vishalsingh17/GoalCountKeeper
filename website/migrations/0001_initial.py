# Generated by Django 2.0.13 on 2019-05-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildTable',
            fields=[
                ('season', models.IntegerField(blank=True, null=True)),
                ('goals', models.IntegerField(blank=True, null=True)),
                ('cid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'child_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerTable',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'player_table',
                'managed': False,
            },
        ),
    ]
