# ---------------------------------- [edit] ---------------------------------- #
from django.shortcuts import render, get_object_or_404, redirect
# ---------------------------------------------------------------------------- #
from ..models import Question, Answer, Comment,Header_home
from django.utils import timezone
from ..forms import QuestionForm, AnswerForm, CommentForm, PostSearchForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.views.generic import FormView
from django.db.models import Q
""" 서치바 기능 도입중 """

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'search.html'
    
    

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Answer.objects.filter(Q(content__icontains=searchWord) | Q(subject__icontains=searchWord)).distinct()
        question_list = Question.objects.order_by('create_date')
        answer_list = Answer.objects.order_by('create_date')

        context = {}
        
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        context['question_list'] = question_list
        context['answer_list'] = answer_list
        
        
        return render(self.request, self.template_name, context)



def index(request):
    """
    pybo 목록 출력
    """
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
        # 조회
    question_list = Question.objects.order_by('create_date')
    answer_list = Answer.objects.order_by('create_date')
    search_url = 'pybo/'
    header_home = Header_home.objects.get(pk=1)

    context = {'question_list': question_list,'answer_list': answer_list,'search_url': search_url,'header_home': header_home}
    return render(request, 'index.html', context)
# ---------------------------------------------------------------------------- #    
def detail(request, answer_id):
    """
    pybo 내용 출력
    """
    
    question_list = Question.objects.order_by('create_date')
    answer_list = Answer.objects.order_by('create_date')
    search_url = '../'
    

    answer = get_object_or_404(Answer, pk=answer_id)
    context = {'answer': answer, 'question_list': question_list,'answer_list': answer_list,'search_url': search_url}
    return render(request, 'index.html', context)