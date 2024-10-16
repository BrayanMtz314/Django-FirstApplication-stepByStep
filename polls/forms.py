from django import forms
from django.utils import timezone
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]
        widgets = {
            "pub_date": forms.DateInput(attrs={"type": "date"})
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["question", "choice_text", "votes"]
