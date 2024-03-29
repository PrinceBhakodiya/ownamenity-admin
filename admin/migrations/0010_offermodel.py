# Generated by Django 5.0.1 on 2024-02-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0009_custmaterial_delete_customermaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferModel',
            fields=[
                ('offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('offer_name', models.CharField(max_length=20)),
                ('p_id', models.IntegerField()),
                ('offer_type', models.CharField(max_length=50)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('isActive', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'offer',
                'managed': False,
            },
        ),
    ]
