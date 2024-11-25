# Generated by Django 5.1.3 on 2024-11-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_habits", "0003_alter_habit_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                blank=True,
                help_text="Укажите вознаграждение",
                max_length=500,
                null=True,
                verbose_name="Вознаграждение",
            ),
        ),
    ]
