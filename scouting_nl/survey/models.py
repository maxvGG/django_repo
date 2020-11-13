from django.db import models
from django import forms
# Create your models here.

MC = 'MC'
CN = 'CN'

CATEGORY = (
    (MC, 'MultipleChoice'),
    (CN, 'Choose Next'),
)

valueA = '1'
valueB = '2'
valueC = '3'
valueD = '4'
valueE = '5'

MULTIPLECHOICE = (
    (valueA, 'is mij onbekend/ kan ik niet'),
    (valueB, 'ik weet ervan, maar heb het nooit gebruikt'),
    (valueC, 'ik weet het en kan het toepassen'),
    (valueD, 'ik kan het toepassen in andere situaties / omstandigheden'),
    (valueE, 'ik kan een ander uitleggen wat het is en hoe je het kan toepassen'),
)

class Questionnaire(models.Model):
    questoinnaire_name = models.CharField(max_length=100,
                                          verbose_name="naam, Vragenlijst",
                                          null=False,
                                          default=None,
                                          blank=False)
    def __str__(self):
        return self.questoinnaire_name

class Question(models.Model):
    questionnaire = models.ManyToManyField(Questionnaire)
    question_text = models.CharField(max_length=200,
                                    verbose_name="naam vraag",
                                    null=True,
                                    default=None,
                                    blank=True)
    question_category = models.CharField(max_length=5,
                                        verbose_name="Question category",
                                        null=False,
                                        choices=CATEGORY,
                                        default=None,
                                        blank=False)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question,
                                on_delete=models.CASCADE)


class MultipleChoiceAnswer(Answer):
    answer = models.IntegerField(choices=MULTIPLECHOICE)
    def __str__(self):
        return self.answer

        