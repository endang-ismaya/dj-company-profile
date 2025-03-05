from django.contrib import admin
from django.core.exceptions import ValidationError
from app.models import GeneralInfo


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
