# Generated by Django 4.0.4 on 2022-05-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_alter_scopeship_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopeship',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope'),
        ),
    ]
