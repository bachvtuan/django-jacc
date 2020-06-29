# Generated by Django 3.0.7 on 2020-06-29 03:46

from django.db import migrations
import jutil.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('jacc', '0021_auto_20191209_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=jutil.modelfields.SafeCharField(blank=True, choices=[('EUR', 'EUR'), ('USD', 'USD')], default='EUR', max_length=3, verbose_name='currency'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default='', max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='description',
            field=jutil.modelfields.SafeCharField(blank=True, default='', max_length=256, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='accountentrysourcefile',
            name='name',
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default='', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='code',
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=32, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='name',
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=64, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='name',
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default='', max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='entrytype',
            name='code',
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=64, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='entrytype',
            name='identifier',
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default='', max_length=40, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='entrytype',
            name='name',
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default='', max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='filename',
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default='', max_length=255, verbose_name='filename'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='notes',
            field=jutil.modelfields.SafeTextField(blank=True, default='', verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default='', max_length=32, verbose_name='invoice number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='state',
            field=jutil.modelfields.SafeCharField(blank=True, choices=[('N', 'Not due yet'), ('D', 'Due'), ('L', 'Late'), ('P', 'Paid')], db_index=True, default='', max_length=1, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=jutil.modelfields.SafeCharField(blank=True, choices=[('I1', 'Invoice'), ('I2', 'Credit Note')], db_index=True, default='I1', max_length=2, verbose_name='type'),
        ),
    ]
