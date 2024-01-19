# Generated by Django 5.0.1 on 2024-01-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=30)),
                ('p_desc', models.CharField(max_length=100)),
                ('p_category_id', models.IntegerField(max_length=5)),
                ('p_curstock', models.IntegerField(max_length=10)),
                ('p_price', models.IntegerField(max_length=10)),
                ('p_rating', models.FloatField()),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='productImageModel',
            fields=[
                ('P_img_id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('P_img_link', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'product_image',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='productModel',
        ),
    ]
