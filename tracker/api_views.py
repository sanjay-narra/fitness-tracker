from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import Workout, Category
from .serializers import WorkoutSerializer, CategorySerializer

class WorkoutListCreateAPI(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(
            user=self.request.user
        ).select_related('category').order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkoutDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def api_summary(request):
    workouts = Workout.objects.filter(user=request.user)
    total_workouts = workouts.count()
    total_minutes = workouts.aggregate(total=Sum('duration'))['total'] or 0
    by_category = workouts.values('category__name').annotate(count=Count('id'))
    return Response({
        'username': request.user.username,
        'total_workouts': total_workouts,
        'total_minutes': total_minutes,
        'total_hours': round(total_minutes / 60, 1),
        'workouts_by_category': list(by_category),
    })