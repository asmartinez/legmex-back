from rest_framework import serializers

from .models import Tpe_col_cattdisp

class Tpe_col_cattdispSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tpe_col_cattdisp
        fields = ('id','dispositionType')