from rest_framework import serializers

from backweb.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Article
        fields = ['id', 'title', 'desc', 'content', 'tags', 'create_time', 'icon', 'column_id']
