# Generated by Django 3.1.7 on 2021-03-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0008_auto_20210330_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='sum',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z1',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z10',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z2',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z3',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z4',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z5',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z6',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z7',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z8',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='tests',
            name='z9',
            field=models.CharField(default='0', max_length=3),
        ),
    ]