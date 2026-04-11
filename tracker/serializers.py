from rest_framework import serializers
from .models import Workout, Category

class CategorySerializer(serializers.ModelSerializer):
    workout_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'color', 'icon', 'workout_count']

    def get_workout_count(self, obj):
        return obj.workouts.count()


class WorkoutSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )
    category_color = serializers.CharField(
        source='category.color',
        read_only=True
    )
    category_icon = serializers.CharField(
        source='category.icon',
        read_only=True
    )
    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Workout
        fields = [
            'id',
            'activity',
            'duration',
            'date',
            'category',
            'category_name',
            'category_color',
            'category_icon',
            'username',
        ]
        read_only_fields = ['id', 'username']