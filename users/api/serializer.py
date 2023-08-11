from rest_framework.serializers import ModelSerializer
from users.models import User

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','username']
    
    def create(self,validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields=['id','email','username','first_name', 'last_name','role']