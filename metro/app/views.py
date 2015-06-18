from django.shortcuts import render

# Create your views here.
from django.conf import settings
from forms import NameForm
from models import Metro
from django.http import HttpResponseRedirect
from forms import DetailsForm
#from models import Details
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse

@login_required 
def form(request):
    if request.method == 'POST':
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            city=form.cleaned_data['city']
            m=Metro()
            m.name=name
            m.city=city
            m.save()
            return HttpResponseRedirect("/show/")

    else:
        form=NameForm()
        

    return render(request,"form.html",locals())
@login_required 
def show(request):

    list=Metro.objects.all()

    return render(request,"show.html",locals())

def delete_new(request,id):
   u = Metro.objects.get(pk=id).delete()
  
   return render(request,"delete.html",locals())

def details_form(request):
    if request.method=="POST":
        form=DetailsForm(request.POST)
        if form.is_valid():
            number=form.cleaned_data['number']
            start_stage=form.cleaned_data['start_stage']
            end_stage=form.cleaned_data['end_stage']
            d=Details()
            d.number=number
            d.start_stage=start_stage
            d.end_stage=end_stage
            d.save()
            return HttpResponseRedirect("/train_details/")
    else:
        form=DetailsForm()
    return render(request,"train_list.html",locals())
def train_list(request):
    list=Details.objects.all()
    return render(request,"train_details.html",locals())

def train_details(request,id):
     u = Details.objects.get(pk=id)

     return render(request,"details.html",locals())
    
def Login(request):
    if request.method=="POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
           from django.contrib import auth
           auth.login(request, user)
    	   return HttpResponseRedirect("/form/")
    	else:
                error = "yes"
		return render(request,"login.html",{'e':error})
    return render(request,"login.html")
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/form/")

def user_details(request):

     list = User.objects.all()

     return render(request,"user_details.html",locals())
    
def test_count_session(request):
    if 'count' in request.session:
        request.session['count'] += 1
        print request.session['count']
        
        return HttpResponse('new count=%s' % request.session['count'])
    else:
        request.session['count'] = 1
        return HttpResponse('No count in session. Setting to 1')
def show_train_list(request):
    list=Details.objects.all()
    return render(request,"show_train_details.html",locals())

def form_edit(request,pk=id):
    if request.POST:
        form=NameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/show/")
    else:
        form=NameForm()
        

    return render(request,"form.html",locals())
    
         



    
