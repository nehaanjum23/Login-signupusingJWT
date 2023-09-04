from rest_framework import serializers
from api.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type' : 'password'}, write_only = True)
    #note: The style attribute is used to specify that this field should be rendered as a password input in user interfaces. The write_only attribute indicates that this field should not be included when serializing the user data (i.e., it's only used during input validation).
    class Meta:
        model = User
        fields = ['email', 'name', 'tc', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    def validate(self, attrs): #note: The validate method is used to perform additional validation on the data before creating a new user. In this case, it checks if the password and password2 fields match. 
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2 :
            raise serializers.ValidationError("Password and confirm password doesn't match")
        return (attrs)
    
    def create(self, validate_data): #note: it is use to create new user
        return User.objects.create_user(**validate_data) #note: It uses the create_user method of the User model manager to create the user with the validated data.

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']
