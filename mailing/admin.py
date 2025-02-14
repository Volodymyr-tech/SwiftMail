from django.contrib import admin

from mailing.models import Mail, MailingAttempt


# Register your models here.
@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('message', 'owner', 'status')
    list_filter = ('status',)

@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('mail', 'owner', 'status', 'server_response')
    list_filter = ('status',)