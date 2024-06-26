# Generated by Django 5.0.3 on 2024-03-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproduct', '0007_remove_sell_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='cost_price',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='harvest_date',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='packaging',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='shelf_life',
        ),
        migrations.AddField(
            model_name='sell',
            name='heading',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sell',
            name='intro',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sell',
            name='picture',
            field=models.ImageField(null=True, upload_to='profile_picture/'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='article',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
