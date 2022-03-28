from rest_framework import serializers
from .models import Student, Timetable
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('stuName', 'id')

class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timetable
        fields = ('date', 'time', 'type', 'location', 'description', 'staff')