# Generated by Django 5.0.1 on 2024-02-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('o_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_no', models.BigIntegerField(unique=True)),
                ('order_exp_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('order_status', models.CharField(max_length=50)),
                ('emp_id', models.IntegerField()),
            ],
            options={
                'db_table': 'order_status',
                'managed': False,
            },
        ),
    ]
