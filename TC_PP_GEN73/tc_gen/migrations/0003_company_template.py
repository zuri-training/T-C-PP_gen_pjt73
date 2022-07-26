# Generated by Django 4.0.6 on 2022-08-09 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tc_gen', '0002_reviews_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_website_name', models.CharField(max_length=50)),
                ('company_website_url', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('company_email_address', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tc_gen.company')),
            ],
        ),
    ]
