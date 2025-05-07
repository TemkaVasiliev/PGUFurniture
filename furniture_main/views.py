from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    context = {}
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data["liked_sections"] = ", ".join(data["liked_sections"])
            context['success'] = True
            context['data'] = data
        else:
            context['success'] = False
    else:
        form = FeedbackForm()
        context['success'] = False

    context['form'] = form
    return render(request, 'pool.html', context)

def about(request):
    return render(request, 'about.html')

def links(request):
    return render(request, 'links.html')

def logout_well(request):
    return render(request, 'logout.html')

