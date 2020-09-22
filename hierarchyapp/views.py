from django.shortcuts import render
from hierarchyapp.models import FileFolder

def index_view(request):
    file_folder = FileFolder.objects.all()
    return render(request, "index.html", {"file_folder": file_folder})
