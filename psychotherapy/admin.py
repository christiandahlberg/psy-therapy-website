from django.contrib import admin
from psychotherapy.models import About, Prices, Frontpage

# Max amount of 'About'-inputs
MAX_OBJECTS = 1

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

class PricesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

class FrontpageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


admin.site.register(About, AboutAdmin)
admin.site.register(Prices, PricesAdmin)
admin.site.register(Frontpage, FrontpageAdmin)

# BASE SETTINGS
admin.site.site_header = "Admin"
admin.site.site_title = "Veronica Käck Admin Portal"
admin.site.index_title = "Welcome to Veronica Käck Admin Portal"