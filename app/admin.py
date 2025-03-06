from django.contrib import admin
from django.core.exceptions import ValidationError
from app.forms import TestimonialForm
from app.models import (
    ContactFormLog,
    FrequentlyAskedQuestion,
    GeneralInfo,
    Service,
    Testimonial,
)


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ["company_name", "location", "email", "phone"]

    def has_add_permission(self, request):
        if GeneralInfo.objects.exists():
            return False  # Disallow adding if a record already exists
        return True

    def save_model(self, request, obj, form, change):
        if not change and GeneralInfo.objects.exists():
            raise ValidationError("Only one record of this type is allowed.")
        super().save_model(request, obj, form, change)

    # show to disable 'add' permission
    # def has_add_permission(self, request):
    #     return False

    # show to disable 'delete' permission
    def has_delete_permission(self, request, obj=None):
        return False

    # show to disable 'change' permission
    # def has_change_permission(self, request, obj=None):
    #     return False

    # show to disable 'view' permission
    # def has_view_permission(self, request, obj=None):
    #     return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["icon", "title", "description"]
    search_fields = ["title", "description"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialForm
    list_display = ["username", "user_job_title", "display_rating_count", "review"]

    def display_rating_count(self, obj):
        return "* " * obj.rating_count

    display_rating_count.short_description = "Rating"


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "answer"]
    search_fields = ["question", "answer"]


@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = ["email", "is_success", "is_error", "action_time"]

    # show to disable 'add' permission
    def has_add_permission(self, request):
        return False

    # show to disable 'delete' permission
    def has_delete_permission(self, request, obj=None):
        return False

    # show to disable 'change' permission
    def has_change_permission(self, request, obj=None):
        return False
