from rest_framework import viewsets

from .serializers import StudentSerializer, TimetableSerializer
from .models import Student, Timetable


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    
class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all().order_by('date')
    serializer_class = TimetableSerializer