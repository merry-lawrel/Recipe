# Generated by Django 4.1.4 on 2023-02-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=10)),
                ('recipe_image', models.ImageField(upload_to='')),
                ('ingredients', models.TextField(max_length=200)),
                ('instructions', models.TextField(max_length=200)),
            ],
        ),
    ]
