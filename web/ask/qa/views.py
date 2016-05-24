from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from qa.models import Question
from qa.forms import AskForm, AnswerForm


def paginate(request, lines, limit=10):
    paginator = Paginator(lines, limit)
    page = request.GET.get('page', 1)
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        raise Http404
    except EmptyPage:
        return paginator.page(paginator.num_pages)


@require_GET
def index(request, *args, **kwds):
    last_questions = Question.objects.order_by('-id')
    context = {'questions': paginate(request, last_questions)}
    return render(request, 'index.html', context)


@require_GET
def popular(request, *args, **kwds):
    popular_questions = Question.objects.order_by('-rating')
    context = {'questions': paginate(request, popular_questions)}
    return render(request, 'list.html', context)


@require_GET
def question(request, slug):
    try:
        id = int(slug)
    except ValueError:
        raise Http404
    question = get_object_or_404(Question, pk=id)
    return render(request, 'single.html', {'question': question})


def ask(request):
    return _post(request, AskForm, 'ask.html')


def answer(request):
    return _post(request, AnswerForm, 'answer.html')


def _post(request, Form, template):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(post.get_url())
    else:
        form = Form()
    return render(request, template, {'form': form})
