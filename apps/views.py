from django.shortcuts import render, redirect
from django.urls import reverse
from httpx import post
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


from apps.models import (
    User,
    Skills,
    Service,
    Priz,
    Portfolio,
    Blog,
    BlogSingle,
    Comment,
    Opinion,
)


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        full_message = f"{email} dan sizga quyidagi habar keldi:\n\n\n{subject}\n\n\n{message}"

        try:
            send_mail(
                f"{name} sizga habar yubordi.",
                full_message,
                settings.EMAIL_HOST_USER,
                [
                    settings.EMAIL_HOST_USER,
                ],
                fail_silently=False,
            )
            return redirect("home")
        except Exception as e:
            print(f"Email yuborishda xato: {e}")
            return HttpResponse(f"Xato yuz berdi : {e}")

    users = User.objects.first()
    skills = Skills.objects.all()
    services = Service.objects.all()
    priz = Priz.objects.all()
    portfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    opinions = Opinion.objects.all()
    # all_users = User.objects.all()
    return render(
        request,
        "index.html",
        {
            "user": users,
            "skills": skills,
            "services": services,
            "prizs": priz,
            "portfolios": portfolio,
            "blogs": blog,
            "opinions": opinions,
        },
    )


def PortfolioDetailsView(request, id):
    portfolios = Portfolio.objects.all()
    portfolio = Portfolio.objects.filter(id=id).first()

    return render(
        request,
        "portfolio-details.html",
        {"portfolio": portfolio, "portfolios": portfolios},
    )


def BlogSingleView(request, id):
    blog_singles = BlogSingle.objects.all()
    blog_single = BlogSingle.objects.filter(id=id).first()
    blog = Blog.objects.first()
    blog_all = Blog.objects.all()
    users = User.objects.first()

    return render(
        request,
        "blog-single.html",
        {
            "blog_singles": blog_singles,
            "blog_single": blog_single,
            "blog": blog,
            "user": users,
            "blog_all": blog_all,
        },
    )


def commentfunc(request, pk):
    blog = Blog.objects.filter(id=pk).first()
    personal_info = User.objects.first()
    if not blog:
        return redirect("error_page")

    if request.POST:
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        post_id = pk
        text = request.POST.get("text")
        if fullname and post_id and text and email:
            Comment.objects.create(
                fullname=fullname, email=email, post_id_id=post_id, text=text
            )
            return redirect(reverse("post", args=(pk,)))

    searchs = ""
    if request.GET:
        key = request.GET.get("s")
        searchs = BlogSingle.objects.filter(title__contains=key)

    comments = Comment.objects.filter(post_id=pk).order_by("created_at")
    return render(
        request,
        "blog-single.html",
        {
            "comments": comments,
            "searchs": searchs,
            "blog": blog,
            "personal_info": personal_info,
        },
    )
