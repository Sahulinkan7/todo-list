from django.shortcuts import render,HttpResponseRedirect
from .models import Task
from .forms import TaskForm
from datetime import date
# Create your views here.

def todohome(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form=TaskForm()
            return HttpResponseRedirect("/")
    else:
        form=TaskForm()
        added_task=Task.objects.filter(is_completed=False)
        completed_task=Task.objects.filter(is_completed=True)
    context={
        'form':form,
        'completed_task':completed_task,
        'pending_task':added_task,
        'date':date.today()
    }
    return render(request,"todoapp/todo-home.html",context)

def delete_task(request,pk):
    if request.method=='POST':
        obj=Task.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect("/")
    
def mark_done(request,pk):
    if request.method=="POST":
        obj=Task.objects.get(pk=pk)
        obj.is_completed=True
        obj.save()
        return HttpResponseRedirect("/")
    
def mark_undone(request,pk):
    if request.method=='POST':
        obj=Task.objects.get(pk=pk)
        obj.is_completed=False
        obj.save()
        return HttpResponseRedirect("/")
    
def edit_task(request,pk):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        obj=Task.objects.get(pk=pk)
        form=TaskForm(instance=obj)
    return render(request,"todoapp/update_task.html",{'form':form})
