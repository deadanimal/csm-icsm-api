# Generated by Django 2.2 on 2020-06-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_auto_20200604_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='name',
            new_name='ceo_name',
        ),
        migrations.AddField(
            model_name='organisation',
            name='address_line_1',
            field=models.CharField(default='NA', max_length=255),
        ),
        migrations.AddField(
            model_name='organisation',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organisation',
            name='city',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='organisation',
            name='country',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisation_email',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisation_fax',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisation_name',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisation_phone',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='organisation',
            name='postcode',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ssm_registration_no',
            field=models.CharField(default='NA', max_length=255),
        ),
        migrations.AddField(
            model_name='organisation',
            name='state',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
