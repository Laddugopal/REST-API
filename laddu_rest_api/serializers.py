from rest_framework import serializers
from laddu_rest_api import models

class HelloSerializer(serializers.Serializer):
    
    '''
        Serializes a name field for APIView testing
    '''
    name = serializers.CharField(max_length = 10)
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    '''serializes a user profile object'''
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
                'password':{
                    'write_only': True,
                        'style':{
                            'input_style': 'password'
                        }
                }
            }
        
    def create(self, validated_data):
        "create and return a new user"
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user