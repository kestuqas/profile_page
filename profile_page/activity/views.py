from django.shortcuts import render
from .models import Post


def activity(request):
	context = {
		'activities': Post.objects.all()
	}
	return render(request, 'activity/activity.html', context)


def about(request):
	return render(request, 'activity/about.html', {'title': 'About me'})

