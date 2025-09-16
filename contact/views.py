# from django.shortcuts import render
# from django.core.mail import send_mail
# from .models import ContactMessage # import the model 

# # Create your views here.
# def contact(request):
#     submitted = False
#     name = ""

#     # Handle form submission
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")
        
#         # Save to DB (database)
#         ContactMessage.objects.create(
#             # field names from models.py
#             name=name, 
#             email=email, 
#             message=message
#             )
        
#         # send email notification to site admin
#         send_mail(
#             subject=f"📩 New Contact Message from {name}",
#             message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
#             from_email=email,
#             recipient_list=["joshuaugwu89@gmail.com"], # add your admin email here

#             fail_silently=False, # raise error if email fails to send 
#         )

#         submitted = True 

#     return render(request, "contact.html", {"submitted": submitted, "name": name})

# from django.core.mail import send_mail
# from django.conf import settings
# from django.shortcuts import render, redirect
# from .models import ContactMessage

# def contact(request):
#     submitted = request.GET.get("submitted", False)  # check query param
#     name = ""

#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")

#         # Save in DB
#         ContactMessage.objects.create(
#             name=name, email=email, message=message
#         )

#         try:
#             # Send notification to YOU (admin)
#             send_mail(
#                 subject=f"📩 New Contact Message from {name}",
#                 message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[settings.EMAIL_HOST_USER],
#                 fail_silently=False,
#             )

#             # Send confirmation back to USER
#             send_mail(
#                 subject="✅ We received your message",
#                 message=(
#                     f"Hello {name},\n\n"
#                     f"Thanks for reaching out! We got your message:\n\n"
#                     f"{message}\n\n"
#                     "We'll reply soon.\n\n- Josh's Django"
#                 ),
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[email],
#                 fail_silently=False,
#             )
#         except Exception as e:
#             print("⚠️ Email send failed:", e)

#         # Redirect to avoid duplicate submissions on refresh
#         return redirect("/contact/?submitted=True")

#     return render(request, "contact.html", {"submitted": submitted, "name": name})




from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import render, redirect
from .models import ContactMessage

def contact(request):
    submitted = request.GET.get("submitted", False)
    name = ""

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save in DB
        ContactMessage.objects.create(
            name=name, email=email, message=message
        )

        try:
            # --- 1. Send notification to YOU (admin) ---
            send_mail(
                subject=f"📩 New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # --- 2. Send confirmation back to USER (HTML email) ---
            subject = "✅ We received your message"
            from_email = settings.EMAIL_HOST_USER
            to = [email]

            text_content = (
                f"Hello {name},\n\n"
                f"Thanks for reaching out! We got your message:\n\n"
                f"{message}\n\n"
                "We'll reply soon.\n\n- Josh's Django"
            )

            logo_url = request.build_absolute_uri("/media/jculogo.png")

            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                    <div style="text-align:center; margin-bottom:20px;">
                        <img src="{logo_url}" alt="Logo" style="max-height:60px;">
                    </div>
                    <h2 style="color: #007bff;">Hi {name},</h2>
                    <p>✅ Thanks for reaching out! We got your message:</p>
                    <blockquote style="border-left: 3px solid #007bff; padding-left: 10px; color: #555;">
                        {message}
                    </blockquote>
                    <p>We’ll get back to you as soon as possible.</p>
                    <p style="margin-top:20px;">Best regards,<br><strong>Josh's Django Team</strong></p>
                </body>
            </html>
            """

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        except Exception as e:
            print("⚠️ Email send failed:", e)

        return redirect("/contact/?submitted=True")

    return render(request, "contact.html", {"submitted": submitted, "name": name})
