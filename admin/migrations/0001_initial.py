# Generated by Django 5.0.1 on 2024-01-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=191, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
    ]
