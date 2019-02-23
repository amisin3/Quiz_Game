from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

User = get_user_model()

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.question_text)


class Answer(models.Model):
    answer_text = models.CharField(max_length=255)
    answer_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    related_to = models.ForeignKey(
        Question, blank=True, null=True, on_delete=models.CASCADE)
    right_ans = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    def update_ans(self):
        self.right_ans = True
        self.save()
    
    def undo_ans(self):
        self.right_ans = False
        self.save()

class Result(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.user.score)

    def get_absolute_url(self):
        return redirect("quizapp:detail", pk=self.pk)


class User_specific_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()