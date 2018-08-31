from rest_framework import viewsets
from appname.models import classname
from appname.serializers import classnameSerializer

class classnameviewsets(viewsets.ModelViewSet):
    serializer_class = classnameSerializer
    queryset = classname.objects.all()