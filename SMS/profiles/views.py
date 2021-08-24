
from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm
from .serializers import ProfileSerializer, HighscoreSerializer
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView

import sys
sys.path.append('..')
from main.models import Puzzle
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


class SolvedByUser(viewsets.ModelViewSet):
	serializer_class = ProfileSerializer
	def get_queryset(self):
		puzzleSlug = self.kwargs.get('puzzleSlug')
		puzzle = Puzzle.objects.get(puzzle_slug=puzzleSlug)
		profile = Profile.objects.get(username=self.request.user.username)
		if puzzle.solvers.filter(pk=self.request.user.pk).exists():
			#puzzle.solvers.remove(self.request.user)
			#print("User Already Exists!")
			pass
		else:
			puzzle.solvers.add(self.request.user)
			profile.XP = profile.XP + puzzle.xps
			profile.puzzles_completed += 1
			xp = profile.XP
			if (xp < 100):
				profile.level = 0
			elif (xp > 100 and xp < 250):
				profile.level = 1
			elif (xp > 250 and xp < 600):
				profile.level = 2
			elif (xp > 600 and xp < 1000):
				profile.level = 3
			elif (xp > 1000 and xp < 1500):
				profile.level = 4
			elif (xp > 1500):
				profile.level = 5


			profile.save()
		
		return  Profile.objects.filter(username=self.request.user.username)
			
	
	authenticationClasses = (TokenAuthentication,)
	permissionClasses = (IsAuthenticated,)

			
class HighscoreboardViewSet(viewsets.ModelViewSet):
	serializer_class = HighscoreSerializer
	def get_queryset(self):
		users = Profile.objects.all().order_by('XP')
		return users[::-1]
	
	authenticationClasses = (TokenAuthentication,)
	permissionClasses = (IsAuthenticated,)

class EditUserViewSet(viewsets.ModelViewSet):
	serializer_class = HighscoreSerializer
	def get_queryset(self):
		users = Profile.objects.all().order_by('XP')
		return users[::-1]
	def put(self, request, *args, **kwargs):
		
		user = Profile.objects.get(user=self.request.user)
		error = "NONE"
		change = "NONE"
		if (len(self.request.data) == 2):
			try:
				info = self.request.data['info']
				languages = self.request.data['languages']
				user.info = info
				user.languages = languages
				user.save()
				change = "CHANGES"
			except Exception as e:
				
				error = str(e)
				
		
		returnData = {'username':user.username,'info': user.info, 'languages':user.languages, 'ERROR':error, 'CHANGE':change}
		return Response(returnData)


    