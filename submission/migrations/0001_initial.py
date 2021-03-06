# Generated by Django 2.1.2 on 2018-12-05 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=20)),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=20)),
                ('language_name', models.CharField(max_length=30, null=True)),
                ('remote_oj', models.CharField(max_length=20, null=True)),
                ('remote_id', models.CharField(max_length=20, null=True)),
                ('remote_run_id', models.CharField(max_length=20, null=True)),
                ('verdict', models.CharField(default='Waiting', max_length=40, null=True)),
                ('verdict_code', models.IntegerField(default=0)),
                ('execute_time', models.CharField(max_length=20, null=True)),
                ('execute_memory', models.CharField(max_length=20, null=True)),
                ('compile_info', models.TextField(null=True)),
                ('sha256', models.CharField(max_length=200, null=True)),
                ('status', models.IntegerField(default=0)),
                ('hook', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'submission',
                'ordering': ('-create_time',),
            },
        ),
    ]
