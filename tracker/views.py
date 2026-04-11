from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.utils import timezone
import json
from .models import Workout, Category
from .forms import WorkoutForm

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(
        user=request.user
    ).select_related('category').order_by('-date')
    categories = Category.objects.all()

    category_filter = request.GET.get('category')
    if category_filter:
        workouts = workouts.filter(category__name__iexact=category_filter)

    return render(request, 'tracker/workout_list.html', {
        'workouts': workouts,
        'categories': categories,
        'selected_category': category_filter,
    })

@login_required
def dashboard(request):
    workouts = Workout.objects.filter(
        user=request.user
    ).select_related('category')

    # --- Stats Cards ---
    total_workouts = workouts.count()
    total_minutes = workouts.aggregate(
        total=Sum('duration')
    )['total'] or 0
    total_hours = round(total_minutes / 60, 1)

    # --- Bar Chart: Last 7 days workout minutes ---
    today = timezone.now().date()
    last_7_days = []
    last_7_minutes = []

    for i in range(6, -1, -1):
        day = today - timezone.timedelta(days=i)
        minutes = workouts.filter(date=day).aggregate(
            total=Sum('duration')
        )['total'] or 0
        last_7_days.append(day.strftime('%a %d'))
        last_7_minutes.append(minutes)

    # --- Doughnut Chart: Workouts by Category ---
    category_data = workouts.values(
        'category__name',
        'category__color'
    ).annotate(count=Count('id')).order_by('-count')

    category_labels = []
    category_counts = []
    category_colors = []

    for item in category_data:
        category_labels.append(item['category__name'] or 'Uncategorized')
        category_counts.append(item['count'])
        category_colors.append(item['category__color'] or '#4361ee')

    # --- Most Active Day ---
    from django.db.models import Count as DCount
    most_active = workouts.values('date').annotate(
        count=DCount('id')
    ).order_by('-count').first()
    most_active_day = most_active['date'].strftime('%B %d, %Y') if most_active else 'No data yet'

    return render(request, 'tracker/dashboard.html', {
        'total_workouts': total_workouts,
        'total_minutes': total_minutes,
        'total_hours': total_hours,
        'most_active_day': most_active_day,
        'last_7_days': json.dumps(last_7_days),
        'last_7_minutes': json.dumps(last_7_minutes),
        'category_labels': json.dumps(category_labels),
        'category_counts': json.dumps(category_counts),
        'category_colors': json.dumps(category_colors),
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