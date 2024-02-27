# Generated by Django 5.0.2 on 2024-02-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0009_merge_20240227_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustMaterial',
            fields=[
                ('Cate_id', models.IntegerField(db_index=True)),
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('material_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cust_martial',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='CustomerMaterial',
        ),
    ]
