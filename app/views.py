from django.shortcuts import render

from app.models import GeneralInfo

"""
company_name = models.CharField(max_length=255, default="Company")
location = models.CharField(max_length=255)
email = models.EmailField()
phone = models.CharField(max_length=20)
open_hours = models.CharField(max_length=100, blank=True, null=True)
video_url = models.URLField(blank=True, null=True)
twitter_url = models.URLField(blank=True, null=True)
facebook_url = models.URLField(blank=True, null=True)
instagram_url = models.URLField(blank=True, null=True)
linkedin_url = models.URLField(blank=True, null=True)
"""


def index(request):
    general_info = GeneralInfo.objects.first()
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
    }
    return render(request, "app/index.html", context)
