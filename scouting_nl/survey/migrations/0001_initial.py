# Generated by Django 3.1.3 on 2020-11-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questoinnaire_name', models.CharField(default=None, max_length=100, verbose_name='naam, Vragenlijst')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.answer')),
                ('answer', models.IntegerField(choices=[('1', 'is mij onbekend/ kan ik niet'), ('2', 'ik weet ervan, maar heb het nooit gebruikt'), ('3', 'ik weet het en kan het toepassen'), ('4', 'ik kan het toepassen in andere situaties / omstandigheden'), ('5', 'ik kan een ander uitleggen wat het is en hoe je het kan toepassen')])),
            ],
            bases=('survey.answer',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='naam vraag')),
                ('question_category', models.CharField(choices=[('MC', 'MultipleChoice'), ('CN', 'Choose Next')], default=None, max_length=5, verbose_name='Question category')),
                ('questionnaire', models.ManyToManyField(to='survey.Questionnaire')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question'),
        ),
    ]
