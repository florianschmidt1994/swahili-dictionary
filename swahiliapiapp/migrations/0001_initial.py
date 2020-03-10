# Generated by Django 3.0.3 on 2020-03-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('english_definition', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('english_example', models.TextField(blank=True, null=True)),
                ('swahili_plural', models.TextField(blank=True, null=True)),
                ('swahili_definition', models.TextField(blank=True, null=True)),
                ('english_word', models.TextField(blank=True, null=True)),
                ('english_plural', models.TextField(blank=True, null=True)),
                ('terminology', models.TextField(blank=True, null=True)),
                ('part_of_speech', models.TextField(blank=True, null=True)),
                ('dialect', models.TextField(blank=True, null=True)),
                ('swahili_word', models.TextField(blank=True, null=True)),
                ('related_words', models.TextField(blank=True, null=True)),
                ('taxonomy', models.TextField(blank=True, null=True)),
                ('derived_word', models.TextField(blank=True, null=True)),
                ('swahili_example', models.TextField(blank=True, null=True)),
                ('derived_language', models.TextField(blank=True, null=True)),
                ('class_field', models.TextField(blank=True, db_column='class', null=True)),
            ],
            options={
                'db_table': 'english',
            },
        ),
        migrations.CreateModel(
            name='Swahili',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('english_definition', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('english_example', models.TextField(blank=True, null=True)),
                ('swahili_plural', models.TextField(blank=True, null=True)),
                ('swahili_definition', models.TextField(blank=True, null=True)),
                ('english_word', models.TextField(blank=True, null=True)),
                ('english_plural', models.TextField(blank=True, null=True)),
                ('terminology', models.TextField(blank=True, null=True)),
                ('part_of_speech', models.TextField(blank=True, null=True)),
                ('dialect', models.TextField(blank=True, null=True)),
                ('swahili_word', models.TextField(blank=True, null=True)),
                ('related_words', models.TextField(blank=True, null=True)),
                ('taxonomy', models.TextField(blank=True, null=True)),
                ('derived_word', models.TextField(blank=True, null=True)),
                ('swahili_example', models.TextField(blank=True, null=True)),
                ('derived_language', models.TextField(blank=True, null=True)),
                ('class_field', models.TextField(blank=True, db_column='class', null=True)),
            ],
            options={
                'db_table': 'swahili',
            },
        ),
    ]
