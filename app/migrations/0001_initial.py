# Generated by Django 3.0.8 on 2020-07-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('brand', models.CharField(max_length=16, verbose_name='品牌')),
            ],
            options={
                'verbose_name': '电脑',
                'verbose_name_plural': '电脑',
                'db_table': 'app_computer',
            },
        ),
    ]
