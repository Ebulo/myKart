# Generated by Django 2.2a1 on 2019-04-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=180)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
