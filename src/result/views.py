# from django import forms
# from django.shortcuts import render

# # Create your views here.
# from .models import Result
# from .form import RawProductForm

# Create your views here.
# def results_list_view(request):
#     results = Result.objects.all
#     return render_to_response(request, "homepage.html", {'results' : results})


# def result_create_view(request):

#     form = RawProductForm()

#     context = {
#         "form": form
#     }

#     return render(request, "guess_form.html", context)