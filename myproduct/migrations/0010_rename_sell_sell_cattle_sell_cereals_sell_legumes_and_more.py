# Generated by Django 5.0.3 on 2024-04-01 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproduct', '0009_rename_article_sell_caption_remove_sell_heading_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sell',
            new_name='Sell_cattle',
        ),
        migrations.CreateModel(
            name='Sell_cereals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('picture', models.ImageField(null=True, upload_to='profile_picture/')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproduct.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sell_legumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('picture', models.ImageField(null=True, upload_to='profile_picture/')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproduct.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sell_poultry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('picture', models.ImageField(null=True, upload_to='profile_picture/')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproduct.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sell_roottubers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('picture', models.ImageField(null=True, upload_to='profile_picture/')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproduct.product')),
            ],
        ),
    ]