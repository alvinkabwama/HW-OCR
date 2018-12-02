from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import UploadFileForm

# Create your views here.
class CharacterExtractor(View):
    def get(self, request):
        return render(request, template_name="image_upload.html")

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)



        result_list = ["Whatever is returned from ML"]
        render(request, template_name="data_view.html", content_type={"resultlist": result_list})
