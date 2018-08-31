from rest_framework import serializers
from appname.models import classname

class classnameSerializer(serializers.ModelSerializer):

    class Meta:
        model = classname
        fields = '__all__'