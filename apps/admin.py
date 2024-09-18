from django.contrib import admin
from .forms import (
    UserForm,
    SkillsForm,
    ServiceForm,
    PrizForm,
    PortfolioForm,
    BlogForm,
    BlogSingleForm,
    OpinionForm,
)
from .models import User, Skills, Service, Priz, Portfolio, Blog, BlogSingle, Opinion


class UserAdmin(admin.ModelAdmin):
    form = UserForm


class SkillsAdmin(admin.ModelAdmin):
    forms = SkillsForm


class ServiceAdmin(admin.ModelAdmin):
    forms = ServiceForm


class PrizAdmin(admin.ModelAdmin):
    forms = PrizForm


class PortfolioAdmin(admin.ModelAdmin):
    forms = PortfolioForm


class BlogAdmin(admin.ModelAdmin):
    forms = BlogForm


class BlogSingleAdmin(admin.ModelAdmin):
    forms = BlogSingleForm
    
class OpinionAdmin(admin.ModelAdmin):
    forms = OpinionForm


admin.site.register(User, UserAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Priz, PrizAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogSingle, BlogSingleAdmin)
admin.site.register(Opinion, OpinionAdmin)
