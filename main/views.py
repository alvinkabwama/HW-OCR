from django.shortcuts import render
from django.views.generic import View
from .forms import UploadFileForm
from django.http import HttpResponse

# Create your views here.
class CharacterExtractor(View):
    def get(self, request):
        return render(request, template_name="image_upload.html")

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            with open('uploads/image.png', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)

            result_list = [{"name": "Kabwama Alvin", "number": 999, "location": "Novia"}]
            return render(request, template_name="data_view.html", content_type={"resultlist": result_list})
        else:
            return HttpResponse("Not so good!")
