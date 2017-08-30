# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase2App', '0007_tabad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postad',
            name='file1',
            field=models.FileField(default='/uploads/LuncClinical.csv', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='postad',
            name='file2',
            field=models.FileField(default='/uploads/geneAnalysis.csv', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='tabad',
            name='category',
            field=models.CharField(choices=[('svmg', 'SVM Gaussian'), ('svml', 'SVM Linear'), ('ann', 'ANN'), ('rfc', 'RFC')], default='svmg', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tabad',
            name='location',
            field=models.CharField(choices=[('uni', 'univariate'), ('pca', 'pca')], default='uni', max_length=500, null=True),
        ),
    ]