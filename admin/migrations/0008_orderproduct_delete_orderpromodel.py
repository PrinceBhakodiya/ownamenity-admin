# Generated by Django 5.0.1 on 2024-02-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0007_complaintmodel_orderpromodel_delete_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(db_index=True)),
                ('p_id', models.IntegerField(db_index=True)),
            ],
            options={
                'db_table': 'order_product',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='orderProModel',
        ),
    ]
