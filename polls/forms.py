from django.forms import ModelForm
from .models import Question, Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
