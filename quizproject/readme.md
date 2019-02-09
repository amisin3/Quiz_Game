# def get_context_data(self, \*\*kwargs):

    #     context = super(Quiz, self).get_context_data(**kwargs)
    #     ques_id = Question.objects.filter(id=1)
    #     print(ques_id)
    #     context['ques'] = ques_id
    #     context['answer'] = Answer.objects.filter(related_to=1)
    #     print(context['answer'])
    #     return context

    # def get_queryset(self):
    #     query = self.request.GET.get('selected')
    #     answer = Answer.objects.filter(related_to=1)
    #     correct_answer = answer.filter(right_ans=True).values('answer_text')
    #     try:
    #         print(correct_answer[0].get('answer_text'))
    #         ans = correct_answer[0].get('answer_text')
    #     except:
    #         print('You have not selected any options')
    #     if query == ans:
    #         print('Answer is correct')
    #         messages.success(self.request,'Your Answer was correct')
    #     else:
    #         print('Answer is incorrect')
    #         messages.warning(self.request, "Your Answer is incorrect")

# def get_context_data(self, \*args, \*\*kwargs):

    #     context = super(QuizDetailView, self).get_context_data(*args, **kwargs)
    #     answer = "Mom"
    #     # answer = Answer.objects.filter(related_to=self.kwargs.get('pk', None))
    #     context['answer'] = answer
    #     return context

    # def get_queryset(self, *args, **kwargs):
    #     query = self.request.GET.get('selected')
    #     # answer = Answer.objects.filter(related_to=self.kwargs.get('pk', None))
    #     print(query)
    #     # correct_answer = answer.filter(right_ans=True).values('answer_text')
    #     # try:
    #     #     ans = correct_answer[0].get('answer_text')
    #     #     if query == ans:
    #     #         messages.success(self.request, "You Got it Right.")
    #     #     else:
    #     #         messages.warning(
    #     #             self.request, "Sorry That was a wrong answer.")

    #     # except:
    #     #     print('You have not selected any option.')
