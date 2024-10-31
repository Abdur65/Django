from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomClaimTokemObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Custom claims
        token['username'] = user.username
        token['email'] = user.email
        
        return token