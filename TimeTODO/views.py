import datetime

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils import timezone

from django.views.generic.edit import CreateView

from .models import TODO
from .form import TODOForm, UserForm, TODOUpdateForm


# Create your views here.

class UpdateView(TemplateView):
    template_name = 'TimeTODO/update.html'


class LoginView(TemplateView):
    template_name = 'registration/login.html'


def signup(request):
    # requst가 POST일 때
    if request.method == "POST":
        # user 폼 지정
        form = UserForm(request.POST)
        print(form)

        # form이 유효할 때
        if form.is_valid():
            # 로컬 DB에 user 저장
            new_user = User.objects.create_user(**form.cleaned_data)
            # home 화면으로 이동
            return render(request, 'registration/success.html')

        # form이 유효하지 않을 때
        else:
            print("사용자 폼 부적합")
            form = UserForm()
            # home 화면으로 이동(로그인 화면)
            return redirect('/')
    else:
        form = UserForm
    return render(request, 'registration/signup.html', {'form': form})


def helloUser(request):
    return HttpResponse("<h1>Hey There User</h1>"
                        "<h2>여기에 TODO LIST 쭉 뽑고 시작!</h2>")


def Index(request):
    if (request.user.id):
        # 로그인 되어있는경우 사용자 정보와 알림 페이지 렌더링
        print(request.user.id)
        TODO_list = TODO.objects.filter(user=request.user)
        finished_TODO = []
        notfinished_TODO = []
        for item in TODO_list:
            if (item.todo_expire_date < timezone.now()):
                if (item.todo_is_finished == True):
                    finished_TODO.append(item)
                elif (item.todo_is_finished == False):
                    notfinished_TODO.append(item)

        print(finished_TODO)
        print(notfinished_TODO)
        return render(request, 'TimeTODO/index.html',
                      {'finished_TODO': finished_TODO,
                       'notfinished_TODO': notfinished_TODO})
        pass
    else:
        # 아닌 경우 로그인 호출
        print(request.user.id)
        return redirect('login')
        pass


def Work(request):
    if (request.user.id):
        prior_todo_list = TODO.objects.filter(todo_is_prior=True, user=request.user)
        common_todo_list = TODO.objects.filter(todo_is_prior=False, user=request.user)
        return render(request, 'TimeTODO/work.html',
                      {'prior_todo_list': prior_todo_list,
                       'common_todo_list': common_todo_list})
    else:
        # 아닌 경우 로그인 호출
        print(request.user.id)
        return redirect('login')


def New(request):
    time = datetime.datetime.now()
    print(time)
    if (request.user.id):
        if request.method == "POST":
            form = TODOForm(request.POST)
            if form.is_valid():
                TODO = form.save(commit=False)
                TODO.user = request.user
                TODO.save()
                return redirect('work')
            else:
                print(form)
                print("form is invaild")
        else:
            form = TODOForm
        return render(request, 'TimeTODO/new.html', {'form': form,
                                                     'time': time})
    else:
        # 아닌 경우 로그인 호출
        print(request.user.id)
        return redirect('login')


def detail(request, todo_id):
    todo = get_object_or_404(TODO, pk=todo_id)
    return render(request, 'TimeTODO/detail.html',
                  {'todo': todo})


def update(request, todo_id):
    todo = TODO.objects.get(pk=todo_id)
    if (request.method == "POST"):
        form = TODOUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('work')
        else:
            print(form)
    else:
        form = TODOUpdateForm
    return render(request, 'TimeTODO/update.html',
                  {'todo': todo, 'form': form})


def delete(request, todo_id):
    TODO.objects.filter(todo_id=todo_id).delete()
    return redirect('work')
