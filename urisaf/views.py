from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UriSAFForm

# Create your views here.
class UrinalysisInput(View):
    def get(self, request):
        return render(request, "data_input.html", {'form': UriSAFForm()})

    def post(self, request):
        form = UriSAFForm(request.POST)
        if form.is_valid():
            input_data = dict(
                leukocytes=form.cleaned_data['leukocytes'],
                nitrates=form.cleaned_data['nitrites'],
                uribilinogen=form.cleaned_data['uribilinogen'],
                protein=form.cleaned_data['protein'],
                pH=form.cleaned_data['pH'],
                blood=form.cleaned_data['blood'],
                specific_gravity=form.cleaned_data['specific_gravity'],
                ketones=form.cleaned_data['ketones'],
                bilirubin=form.cleaned_data['bilirubin'],
                glucose=form.cleaned_data['glucose']
            )
        return redirect("urisaf-results")
        

class UrinalysisResults(View):
    def get(self, request):
        analysis_results = dict(
            disease_name='diseases name',
            affected_parts='affected parts',
            other_parameters='others parameters allowed ...'
        )
        return render(request, "data_display.html", {'analysis_results': analysis_results})
