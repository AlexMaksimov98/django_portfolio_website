# Generated by Django 4.1.3 on 2022-11-04 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_skill', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.skilltype'),
        ),
    ]
