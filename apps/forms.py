from django import forms
from apps.models import (
    User,
    Skills,
    Service,
    Priz,
    Portfolio,
    Blog,
    BlogSingle,
    Opinion,
)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "job",
            "email",
            "phone_number",
            "image",
            "about_me",
        )


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ("title", "level")


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("title", "short_comment")


class PrizForm(forms.ModelForm):
    class Meta:
        model = Priz
        fields = ("title", "num")


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogSingleForm(forms.ModelForm):
    class Meta:
        model = BlogSingle
        fields = "__all__"


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = "__all__"
