from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm
from .serializers import ProfileSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


def my_profile_view(request):
	profile = Profile.objects.get(user=request.user)
	form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
	confirm = False

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			confirm = True

	context = {
		'profile' : profile,
		'form': form,
		'confirm': confirm,
	}

	return render(request, 'profiles/myprofile.html', context)



# Create your views here.
# ViewSets define the view behavior.

class ProfileViewSet(viewsets.ModelViewSet):
	serializer_class = ProfileSerializer
	
	def get_queryset(self):
		name = self.kwargs.get('username')
		if (name == 'me'):
			name = self.request.user.username
		else:
			pass
			
		profile = Profile.objects.filter(username=name)
		return profile

	authenticationClasses = (TokenAuthentication,)
	permissionClasses = (IsAuthenticated,)



    