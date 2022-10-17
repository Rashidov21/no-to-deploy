# Generated by Django 3.2.6 on 2022-10-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer_1', models.CharField(max_length=200)),
                ('answer_2', models.CharField(max_length=200)),
                ('answer_3', models.CharField(max_length=200)),
                ('answer_4', models.CharField(max_length=200)),
                ('right_answer', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]