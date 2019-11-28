# Generated by Django 2.2.7 on 2019-11-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=60)),
                ('Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog', models.TextField(max_length=1000)),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FatherName', models.CharField(max_length=50)),
                ('Citizenship', models.IntegerField()),
                ('Relationof', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.UserDetail')),
            ],
        ),
    ]
