# Generated by Django 4.0.4 on 2022-05-21 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scopeship_article_alter_scopeship_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopeship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scopeship',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope'),
        ),
    ]
