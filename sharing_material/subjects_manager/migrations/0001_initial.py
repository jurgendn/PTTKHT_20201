# Generated by Django 3.1.4 on 2021-01-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('IdAd', models.CharField(max_length=200)),
                ('Date', models.DateTimeField()),
                ('School', models.CharField(max_length=200)),
            ],
        ),
    ]
