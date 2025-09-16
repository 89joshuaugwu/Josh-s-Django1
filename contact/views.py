from django.shortcuts import render
from .models import ContactMessage # import the model 

# Create your views here.
def contact(request):
    submitted = False
    name = ""

    # Handle form submission
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # Save to DB (database)
        ContactMessage.objects.create(
            # field names from models.py
            name=name, 
            email=email, 
            message=message
            )

        submitted = True 

    return render(request, "contact.html", {"submitted": submitted, "name": name})