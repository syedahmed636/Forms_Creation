# Generated by Django 3.0.2 on 2020-07-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=50)),
                ('Incident_Desc', models.CharField(max_length=200)),
                ('Incident_Loc', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('Initial_Security', models.CharField(max_length=50)),
                ('Suspected_Cause', models.CharField(max_length=100)),
                ('Actions', models.CharField(max_length=200)),
                ('Incident_Type', models.CharField(max_length=20)),
                ('Reported_by', models.CharField(max_length=50)),
            ],
        ),
    ]
