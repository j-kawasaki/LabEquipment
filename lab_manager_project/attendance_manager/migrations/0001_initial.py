# Generated by Django 2.1.7 on 2019-02-24 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('sex', models.IntegerField(editable=False)),
                ('grade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance_manager.Person')),
            ],
        ),
    ]
