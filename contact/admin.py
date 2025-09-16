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