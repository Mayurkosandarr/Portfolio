# Generated by Django 5.1.3 on 2024-11-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='aboutme',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='name',
            field=models.CharField(default='mk', max_length=100),
        ),
    ]
