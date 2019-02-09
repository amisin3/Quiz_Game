from django import forms
from .models import Question, Answer


class CreateTestForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)


# class CreateTestFormAns(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ('answer_text',)
    
