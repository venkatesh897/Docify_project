from django.shortcuts import render,HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.core.files.storage import FileSystemStorage





# Create your views here.


def index(request):

	return render(request, 'index.html')

def uploadFile(request):
	return render(request, "file_upload.html")


@csrf_exempt

def uploadFileSave(request):

	print(request.POST)
	print(request.FILES)
	file = request.FILES["file"]
	fs = FileSystemStorage()
	file_path = fs.save(file.name, file)
	print(file_path)
	return HttpResponse("uploded")




