# Django
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

# restframework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')  # Redirect to login page after registration
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    
@permission_required('user.can_view_mymodel', raise_exception=True)
def mymodel_view(request):
    return HttpResponse("This is a restricted view for users with the 'can_view_mymodel' permission.")



# # Open Django shell
# python manage.py shell

# # Assign permission to a specific user
# from django.contrib.auth.models import User, Permission
# from django.contrib.contenttypes.models import ContentType
# from app_name.models import MyModel

# # Get the user and permission
# user = User.objects.get(username='username')
# content_type = ContentType.objects.get_for_model(MyModel)
# permission = Permission.objects.get(codename='can_view_mymodel', content_type=content_type)

# # Add permission to user
# user.user_permissions.add(permission)
