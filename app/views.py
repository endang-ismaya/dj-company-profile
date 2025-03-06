from django.shortcuts import redirect, render
from app.models import GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion as FAQ
from django.contrib import messages


def index(request):
    general_info = GeneralInfo.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    context = {
        "company_name": general_info.company_name,
        "location": general_info.location,
        "email": general_info.email,
        "phone": general_info.phone,
        "open_hours": general_info.open_hours,
        "video_url": general_info.video_url or "#",
        "twitter_url": general_info.twitter_url or "#",
        "facebook_url": general_info.facebook_url or "#",
        "instagram_url": general_info.instagram_url or "#",
        "linkedin_url": general_info.linkedin_url or "#",
        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
    }
    return render(request, "app/index.html", context)


def contact_form(request):
    if request.method == "GET":
        pass

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # skip email configuration from now
        # just sending message
        messages.success(request, f"{name} {email} {subject} {message}")

    return redirect("app__index")
