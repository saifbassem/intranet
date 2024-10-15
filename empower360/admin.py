from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Questionnaire, Question, QuestionLink, Choice

admin.site.disable_action("delete_selected")




class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ("name", "status")

    def has_delete_permission(self, request, obj=None):
        return False
class QuestionLinkAdmin(admin.ModelAdmin):
    exclude = ["answer"]


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question)
admin.site.register(QuestionLink, QuestionLinkAdmin)
admin.site.register(Choice)

