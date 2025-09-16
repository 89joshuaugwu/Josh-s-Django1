from django.contrib import admin
from .models import ContactMessage

# Register your models here.
@admin.register(ContactMessage) # Register the ContactMessage model with the admin site

# Customize the admin interface for ContactMessage
class ContactMessageAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message') # Add search functionality
    list_filter = ('created_at',) # Add filter by creation date
    ordering = ('-created_at',) # Order by creation date descending


# from django.contrib import admin
# from .models import ContactMessage

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "short_message", "created_at")
#     search_fields = ("name", "email", "message")
#     list_filter = ("created_at",)
#     readonly_fields = ("created_at",)
#     ordering = ("-created_at",)

#     # Organize fields in sections
#     fieldsets = (
#         ("Sender Information", {
#             "fields": ("name", "email")
#         }),
#         ("Message Content", {
#             "fields": ("message",)
#         }),
#         ("Meta Data", {
#             "fields": ("created_at",),
#             "classes": ("collapse",),  # collapsible section
#         }),
#     )

#     def short_message(self, obj):
#         return (obj.message[:50] + "...") if len(obj.message) > 50 else obj.message
#     short_message.short_description = "Message"



# from django.contrib import admin
# from .models import ContactMessage

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "short_message", "created_at")
#     search_fields = ("name", "email", "message")
#     list_filter = ("created_at",)
#     readonly_fields = ("created_at",)
#     ordering = ("-created_at",)

#     # Organize fields in sections
#     fieldsets = (
#         ("Sender Information", {
#             "fields": ("name", "email")
#         }),
#         ("Message Content", {
#             "fields": ("message",)
#         }),
#         ("Meta Data", {
#             "fields": ("created_at",),
#             "classes": ("collapse",),  # collapsible section
#         }),
#     )

#     def short_message(self, obj):
#         return (obj.message[:50] + "...") if len(obj.message) > 50 else obj.message
#     short_message.short_description = "Message"




# from django.contrib import admin
# from .models import ContactMessage

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "short_message", "created_at")
#     search_fields = ("name", "email", "message")
#     list_filter = ("created_at",)
#     readonly_fields = ("created_at",)
#     ordering = ("-created_at",)

#     # Organize fields in sections
#     fieldsets = (
#         ("Sender Information", {
#             "fields": ("name", "email")
#         }),
#         ("Message Content", {
#             "fields": ("message",)
#         }),
#         ("Meta Data", {
#             "fields": ("created_at",),
#             "classes": ("collapse",),  # collapsible section
#         }),
#     )

#     def short_message(self, obj):
#         return (obj.message[:50] + "...") if len(obj.message) > 50 else obj.message
#     short_message.short_description = "Message"

