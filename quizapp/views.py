from django.shortcuts import render, redirect
from django.views import generic
from .models import Question, Answer, Result
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
# from .forms import CreateTestForm
# Create your views here.


def start_page(request):
    
    return render(request, "quizapp/startpage.html", {})


def list_page(request):
    quest = Question.objects.filter(pk=1)
    quest_pk = quest.values('pk')[0].get('pk')
    print(quest_pk)
    if request.POST:
        name  = request.POST.get('username')
        print(name)
        if name == '' or name == None:
            messages.error(request, "Please enter a username")
        else:
            messages.success(request, "Username is: %s"%name)
            return redirect('quizapp:detail', pk=quest_pk)
    context = {
        'pk': quest_pk,
        'question': quest,
        }
    return render(request, 'quizapp/startpage.html', context)
    # q = quest.values('question_text')
    

def create_list(request):
    quest = Question.objects.filter(pk=1)
    quest_pk = quest.values('pk')[0].get('pk')
    print(quest_pk)
    # q = quest.values('question_text')
    if request.POST:
        name  = request.POST.get('username')
        print(name)
        if name == '' or name == None:
            messages.error(request, "Please enter a username")
        else:
            messages.success(request, "Username is: %s"%name)
            return redirect('quizapp:create', pk=quest_pk)
    context = {
        'pk': quest_pk,
        'question': quest,
    }
    return render(request, 'quizapp/temp.html', context)


class Quiz(generic.ListView):
    model = Question
    template_name = 'quizapp/question_list.html'


class QuizDetailView(generic.DetailView):
    model = Question
    template_name = 'quizapp/question_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuizDetailView, self).get_context_data(*args, **kwargs)
        answer = Answer.objects.filter(related_to=self.kwargs.get('pk'))
        context['answer'] = answer
        return context

    # def get_queryset(self):
    #     try:
    #         radio = self.request.GET.get('selected')
    #         print(radio)
    #     except (TypeError, Answer.DoesNotExist):
    #         messages.warning('Select the items please')
    #     print(self.kwargs.get('pk'))
    #     answer = Answer.objects.filter(related_to=self.kwargs.get('pk'))
    #     print(answer)
    #     correct_answer = answer.filter(right_ans=True).values('answer_text')
    #     ans = correct_answer[0].get('answer_text')
    #     print(ans)
    #     if ans == radio:
    #         print('You Got It Correct')
    #         messages.success(self.request, 'You Got It Correct')
    #     else:
    #         print('Sorry You Got It Wrong')
    #         messages.warning(self.request, 'Sorry You Got It Wrong')


points = 0


def choice(request, pk):
    question = get_object_or_404(Question, pk=pk)
    global points
    if question == 1:
        points = 0

    try:
        # print(question.answer_set.get(pk=request.GET.get('choice')))
        # selected_choice = question.answer_set.get(pk=request.GET.get('choice'))
        selected_choice = request.GET.get('choice')
        selected_ans = Answer.objects.filter(pk=selected_choice).values('answer_text')[0].get('answer_text')
        # print(selected_ans1)
        # print(selected_choice)
        # print(selected_choice1)
        # selected_ans = request.GET.get('answer_text')
        # print(selected_ans)
        # print(request.GET.get('choice'))
    except (TypeError, Answer.DoesNotExist):
        messages.warning(request, 'Select the choice first')
    else:
        answer = Answer.objects.filter(related_to=pk)
        # print(answer)
        correct_answer = answer.filter(right_ans=True).values('answer_text')
        # print(correct_answer)
        ans = correct_answer[0].get('answer_text')
        print(ans)
        # print(ans)
        new_pk = int(pk)+1
        # print(selected_choice, ans)
        if ans == selected_ans:
            messages.success(request, "you got it correct")
            print('right')
            points = points + 1
            print(points)
        else:
            messages.warning(request, 'sorry you got it wrong')
            print('wrong')

    if new_pk <= 10:
        return redirect('quizapp:detail', pk=new_pk)
    else:
        p = Result(score=points)
        p.save()
        return redirect('quizapp:results')

class ResultsView(generic.ListView):
    model = Result
    template_name = 'quizapp/results.html'



def create_test_view(request, pk):
    quest_pk = pk
    # print(quest_pk)
    quest = Question.objects.filter(pk=quest_pk)
    quest_text = quest.values('question_text')[0].get('question_text')
    # print(quest_text)

    ans = Answer.objects.filter(related_to=quest_pk)
    # print(ans)
    context = {
        'quest': quest_text,
        'ans': ans,
    }
    if request.POST:
        correct_ans = request.POST.get('choose')
        # try_ans = request.POST.get('try')
        # print("This is what i want")
        # print(try_ans)
        # print(correct_ans)
        if correct_ans:
            # print(ans.get(right_ans=True).exists())
            # if ans.get(right_ans=True):
            #     prev_ans = ans.get(right_ans=True)
            # # print(prev_ans)
            # if prev_ans == None:
            #     new_pk = int(pk) + 1
            #     new_ans = ans.get(answer_text=correct_ans)
            #     new_ans.update_ans()
            # elif prev_ans != correct_ans:
            #     new_pk = int(pk) + 1
            #     new_ans = ans.get(answer_text=correct_ans)
            #     # print(new_ans)
            #     new_ans.update_ans()
            #     prev_ans.undo_ans()
            new_pk = int(pk) + 1
            new_ans = ans.get(answer_text=correct_ans)
            new_ans.update_ans()
            answer = Answer.objects.filter(answer_text=correct_ans)
            answer.right_ans = True
        if new_pk <= 10:
            return redirect("quizapp:create", pk=new_pk)
        else:
            return redirect("index")
    return render(request, 'quizapp/createtest.html', context=context)
    # form = CreateTestForm(request.POST or None)
    # context = {
    #     'form': form,
    # }
    # return render(request, 'quizapp/createtest.html', context=context)