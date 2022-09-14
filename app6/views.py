from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import*
from . forms import car1,car2,carForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def a2(request):
    cd=cardata.objects.all()
    return render(request,'index.html',{'c':cd}) 

@login_required(login_url='login')

def a3(request,pid):
    xm=cardata.objects.get(id=pid)
    return render(request,'dview.html',{'x':xm})

@login_required(login_url='login')

def carEdit(request,pid):
    es=get_object_or_404(cardata,id=pid)
    ed=carForm(request.POST or None,instance=es)
    if ed.is_valid():
        ed.save()
        return redirect('/')
    return render(request,'edit.html',{'e':ed})

@login_required(login_url='login')

def carDel(request,cid):
    es=get_object_or_404(cardata,id=cid)
    es.delete()
    return redirect('/')

@login_required(login_url='login')

def carUp(request):
    if request.method=='POST':
        pcar=cardata()
        pcar.name=request.POST['name']
        pcar.dis=request.POST['dis']
        pcar.image=request.FILES['image']
        pcar.save()
        return redirect('/')
    return render(request,'upcar.html')

@login_required(login_url='login')    

def cedit(request,bid):
    cb=get_object_or_404(cardata,id=bid)
    vc=car1(request.POST or None,instance=cb)
    imd=car2(request.POST or None,request.FILES,instance=cb)
    if vc.is_valid():
        if imd.is_valid():
            imd.save()
            vc.save()
            return redirect('/')
        else:
            vc.save()
            return redirect('/')
    return render(request,'upedit.html',{'c':cb ,'im':imd})
    


        