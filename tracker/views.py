from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, Category
from .forms import WorkoutForm

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).select_related('category').order_by('-date')
    categories = Category.objects.all()

    # Filter by category if selected
    category_filter = request.GET.get('category')
    if category_filter:
        workouts = workouts.filter(category__name__iexact=category_filter)

    return render(request, 'tracker/workout_list.html', {
        'workouts': workouts,
        'categories': categories,
        'selected_category': category_filter,
    })

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'tracker/add_workout.html', {'form': form})

@login_required
def edit_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'tracker/edit_workout.html', {'form': form})

@login_required
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'tracker/delete_workout.html', {'workout': workout})