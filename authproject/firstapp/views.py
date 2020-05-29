from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from firstapp.forms import signupform,DocumentForm,DataForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Content1,Document,Simple,Data,Catch,Files
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def home_view(request):
    return render(request,"firstapp/home.html")
def help_view(request):
    return render(request,"firstapp/help.html")
def contact_view(request):
    return render(request,"firstapp/contact.html")
def mysql_view(request):
    return render(request,"firstapp/mysql.html")
def logout_view(request):
    return render(request,"firstapp/home.html")
def django_view(request):
    return render(request,"firstapp/django.html")
def signup_view(request):
    form=signupform()
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
          user=form.save()
          user.set_password(user.password)
          user.save()
        return HttpResponseRedirect("/accounts/login")
    return render(request,"firstapp/signup.html",{"form":form})
def contact1_view(request):
    if request.method=="POST":
        nam=request.POST["name"]
        emai=request.POST["email"]
        massag=request.POST["massage"]
        data=Content1(Name=nam,Email=emai,Massage=massag)
        data.save()
        return render(request,"firstapp/contact1.html")
    return render(request,"firstapp/contact1.html")
def loading_view(request):
    return render(request,"firstapp/loading.html")
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        x=Catch(image=uploaded_file_url)
        x.save()
        return render(request,'firstapp/simple_upload.html',{'uploaded_file_url': uploaded_file_url})
    return render(request, 'firstapp/simple_upload.html')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = DocumentForm()
    return render(request, 'firstapp/model_form_upload.html',{'form': form})
def display_info(request):
    objs=Document.objects.all()
    return render(request,'firstapp/display.html',{'objs':objs})
def data_info(request):
    form = DataForm()
    if request.method=='POST':
        dat=request.POST['data']
        x=Data(data=dat)
        x.save()
    return render(request,"firstapp/data.html",{"form":form})
def dataa_info(request):
    dataa=Data.objects.all()
    return render(request,"firstapp/data1.html",{"dataa":dataa})
def Catch_info(request):
    catch=Catch.objects.all()
    return render(request,"firstapp/raju.html",{"catch":catch})
def simple1_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        y=Files(image=uploaded_file_url)
        y.save()
        return render(request,'firstapp/simple_upload.html',{'uploaded_file_url': uploaded_file_url})
    return render(request, 'firstapp/simple_upload.html')
def Files_info(request):
    files=Files.objects.all()
    return render(request,"firstapp/raju1.html",{"files":files})
@staff_member_required
def Admin_info(request):
    return render(request,"firstapp/mdmd.html")
def Queries_info(request):
    queries=Content1.objects.all()
    return render(request,"firstapp/java.html",{"queries":queries})
def Donate_info(request):
    return render(request,"firstapp/Donate.html")