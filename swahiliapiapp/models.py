# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class English(models.Model):
    id = models.IntegerField(primary_key=True)
    english_definition = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    english_example = models.TextField(blank=True, null=True)
    swahili_plural = models.TextField(blank=True, null=True)
    swahili_definition = models.TextField(blank=True, null=True)
    english_word = models.TextField(blank=True, null=True)
    english_plural = models.TextField(blank=True, null=True)
    terminology = models.TextField(blank=True, null=True)
    part_of_speech = models.TextField(blank=True, null=True)
    dialect = models.TextField(blank=True, null=True)
    swahili_word = models.TextField(blank=True, null=True)
    related_words = models.TextField(blank=True, null=True)
    taxonomy = models.TextField(blank=True, null=True)
    derived_word = models.TextField(blank=True, null=True)
    swahili_example = models.TextField(blank=True, null=True)
    derived_language = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True,
                                   null=True)  # Field renamed because it was a Python reserved word.

    def related_word_list(self):
        return self.related_words.split(", ")

    def __str__(self):
        return self.english_word

    class Meta:
        db_table = 'english'


class Swahili(models.Model):
    id = models.IntegerField(primary_key=True)
    english_definition = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    english_example = models.TextField(blank=True, null=True)
    swahili_plural = models.TextField(blank=True, null=True)
    swahili_definition = models.TextField(blank=True, null=True)
    english_word = models.TextField(blank=True, null=True)
    english_plural = models.TextField(blank=True, null=True)
    terminology = models.TextField(blank=True, null=True)
    part_of_speech = models.TextField(blank=True, null=True)
    dialect = models.TextField(blank=True, null=True)
    swahili_word = models.TextField(blank=True, null=True)
    related_words = models.TextField(blank=True, null=True)
    taxonomy = models.TextField(blank=True, null=True)
    derived_word = models.TextField(blank=True, null=True)
    swahili_example = models.TextField(blank=True, null=True)
    derived_language = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True,
                                   null=True)  # Field renamed because it was a Python reserved word.

    def __str__(self):
        return self.swahili_word

    class Meta:
        db_table = 'swahili'
