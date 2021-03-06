# Generated by Django 2.2.6 on 2020-06-08 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('timing', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=10, null=True)),
                ('height', models.CharField(max_length=10, null=True)),
                ('weight', models.CharField(max_length=10, null=True)),
                ('doj', models.DateField(max_length=10, null=True)),
                ('dob', models.DateField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Batch')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('price', models.CharField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('price', models.CharField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=10, null=True)),
                ('doj', models.DateField(max_length=10, null=True)),
                ('dob', models.DateField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.TimeField(null=True)),
                ('day1', models.CharField(max_length=20, null=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Activity')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dot', models.DateField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='TempCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PackageActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Activity')),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Package')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Product')),
            ],
        ),
        migrations.CreateModel(
            name='MemberPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop', models.DateField(null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Member')),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Package')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='BatchTrainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20, null=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Activity')),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Batch')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='BatchActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.FileField(null=True, upload_to='')),
                ('date1', models.DateField(null=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Activity')),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend', models.CharField(max_length=20, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Member')),
                ('time_table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.TimeTable')),
            ],
        ),
    ]
