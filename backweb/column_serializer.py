from rest_framework import serializers
from backweb.models import Column


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        # 序列化的模型
        model = Column
        # 需要序列化的字段
        fields = ['id', 'c_name']
