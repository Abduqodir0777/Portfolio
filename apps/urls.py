from django.urls import path
from apps.views import home, PortfolioDetailsView, BlogSingleView, commentfunc

urlpatterns = [
    path("", home, name="home"),
    path("portfolio_details/<int:id>", PortfolioDetailsView, name="portfolio_details"),
    path("blog_single/", BlogSingleView, name="blog_single"),
    path('post/<int:pk>/', commentfunc, name='post'),
]
