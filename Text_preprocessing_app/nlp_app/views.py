from django.shortcuts import render

from .nlp_utils import process_text

def home(request):
    if request.method == "POST":
        user_text = request.POST.get("user_text", "")
        processed_text = process_text(user_text)
        return render(request, "home.html", {"processed_text": processed_text, "user_text": user_text})
    return render(request, "home.html")
