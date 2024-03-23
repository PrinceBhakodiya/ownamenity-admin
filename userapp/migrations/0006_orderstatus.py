# Generated by Django 5.0.2 on 2024-02-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_orderproduct_orders_delete_ordersmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('o_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_exp_date', models.DateField(auto_now_add=True, db_column='order_exp_date')),
                ('delivery_date', models.DateField(auto_now_add=True, db_column='delivery_date')),
                ('order_status', models.TextField(db_column='order_status')),
            ],
            options={
                'db_table': 'order_status',
                'managed': False,
            },
        ),
    ]