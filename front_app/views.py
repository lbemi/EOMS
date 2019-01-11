from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import ListView
from .models import *
from .forms import UserForm
from django.contrib import auth
import time
from django.contrib.auth.decorators import login_required

def Login(request):
    nowtime  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'login.html', {'uf': form, 'nowtime': nowtime})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = auth.authenticate(username=username, password= password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('index/')
            else:
                return render(request, 'login.html',{'uf':form,'nowtime':nowtime,'password_is_wrong': True})
        else:
            return render(request,'login.html',{'uf': form, 'nowtime': nowtime})

# @login_required(login_url="/")
class Index_List(ListView):
    model = Host
    template_name = 'base.html'
    paginate_by = 5
    queryset = Host.objects.all().order_by('-host_id')

@login_required
def logout(req):
    auth.logout(req)
    return HttpResponseRedirect('/')