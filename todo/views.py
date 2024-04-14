from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'todo/task_list.html', {'tasks': tasks})
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})
def complete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
        return JsonResponse({'message': 'Task marked as completed.'})
    return JsonResponse({'error': 'Invalid request.'}, status=400)
def completed_task_list(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'todo/completed_task_list.html', {'completed_tasks': completed_tasks})