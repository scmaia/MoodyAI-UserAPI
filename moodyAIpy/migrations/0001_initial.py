# Generated by Django 4.0.4 on 2022-05-31 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('init_date', models.DateTimeField(verbose_name='date of initial signup')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=400)),
                ('response', models.CharField(max_length=400)),
                ('mood', models.CharField(max_length=100)),
                ('favorite', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodyAIpy.user')),
            ],
        ),
    ]
