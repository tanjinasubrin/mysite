from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import Question
from django.views import View


# Create your views here.
class QuestionView(View):
    def get(self, request):
        form  = QuestionForm()
        questions = Question.objects.all()
        return render(request, "index.html", {
            "form": form, 
            "questions": questions
        })
        
    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('question-index')
