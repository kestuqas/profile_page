from django.shortcuts import render

posts = [
	{
		'author': 'kestuqas',
		'title': 'Trial post 1',
		'content': 'First post content',
		'date_posted': '2019-09-05'
	},
	{
		'author': 'mazukas',
		'title': 'Trial post 2',
		'content': 'Second post content',
		'date_posted': '2019-09-06'
	}
]


def trial(request):
	context = {
		'posts': posts
	}

	return render(request, 'trial/home.html', context)


def about(request):
	return render(request, 'trial/about.html', {'title': 'About'})


# Create your views here.
