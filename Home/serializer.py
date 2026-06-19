# from rest_framework import serializers
# from .models import WatchList, StreamPlatform, Review
# import re

# class StreamPlatformSerializer(serializers.ModelSerializer):

#     class Meta:
#         model= StreamPlatform
#         # exclude= ['created']
#         fields= "__all__"
    
#     def validate(self, data):
#         if not re.match(r'^[A-Za-z0-9 ]+$', data['pname']):
#             raise serializers.ValidationError({'pname': 'Only alphabets ,numbers and spaces are allowed'})
        
#         if self.instance is None:
#             print("Put is being checked")
#             if StreamPlatform.objects.filter(pname=data['pname']).exists():
#                 raise serializers.ValidationError({'pname':'Already Exists'})
#         return data

# class WatchListSerializer(serializers.ModelSerializer):
#     platform_details = StreamPlatformSerializer(
#         source='platform',
#         read_only=True
#     )
    
#     class Meta:
#         model= WatchList
#         exclude= ['created']
#         # fields= "__all__"
#         # depth=1
    
#     def validate(self, data):
#         title=data.get('title')
#         if title:
#             if not re.match(r'^[A-Za-z0-9 ]+$', data['title']):
#                 raise serializers.ValidationError({'title': 'Only alphabets ,numbers and spaces are allowed'})
            
#             if self.instance is None:
#                 print("Put is being checked")
#                 if WatchList.objects.filter(title=data['title']).exists():
#                     raise serializers.ValidationError({'title':'Already Exists'})
#         return data


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = "__all__"



from rest_framework import serializers
from .models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    watchlist = serializers.PrimaryKeyRelatedField(read_only=True)
    description = serializers.CharField(required=True)
    
    class Meta:
        model = Review
        fields = ['id', 'review_user', 'rating', 'description', 'watchlist']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def validate(self, attrs):
        # Object-level check: same user can't review the same watchlist twice
        watchlist = self.context['view'].kwargs.get('pk')
        review_user = self.context['request'].user
        if Review.objects.filter(watchlist=watchlist, review_user=review_user).exists():
            raise serializers.ValidationError("You have already reviewed this watchlist.")
        return attrs

    def create(self, validated_data):
        watchlist_id = self.context['view'].kwargs['pk']
        review_user = self.context['request'].user
        watchlist = WatchList.objects.get(pk=watchlist_id)
        return Review.objects.create(
            watchlist=watchlist,
            review_user=review_user,
            **validated_data
        )


class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = ['id', 'title', 'storyline', 'active', 'platform', 'len_name']

    def get_len_name(self, object):
        return len(object.title)


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = ['id', 'pname', 'about', 'website', 'watchlist']