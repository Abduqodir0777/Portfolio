from django.db.models import (
    Model,
    CharField,
    EmailField,
    ForeignKey,
    CASCADE,
    PositiveIntegerField,
    ImageField,
    TextField,
    ImageField,
    URLField,
    DateTimeField,
)


# Create your models here.
class User(Model):
    first_name = CharField(max_length=150, null=True, blank=True)
    last_name = CharField(max_length=150, null=True, blank=True)
    job = CharField(max_length=150, null=True, blank=True)
    phone_number = CharField(max_length=30, null=True, blank=True)
    username = CharField(max_length=140, null=True, blank=True, unique=True)
    email = EmailField(null=True, blank=True)
    image = ImageField(null=True, blank=True)
    about_me = TextField(null=True, blank=True)

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Skills(Model):
    user = ForeignKey("apps.User", on_delete=CASCADE)
    title = CharField(verbose_name="skill nomi", max_length=150)
    level = PositiveIntegerField(default=0)


class Service(Model):
    title = CharField(max_length=150, null=True, blank=True)
    short_comment = TextField(null=True, blank=True)


class Priz(Model):
    title = CharField(max_length=111, null=True, blank=True)
    num = PositiveIntegerField(default=0)


class Portfolio(Model):
    image_main = ImageField(null=True, blank=True, upload_to="portfolio")
    image_details = ImageField(null=True, blank=True, upload_to="portfolio_details")
    name = CharField(max_length=100, null=True, blank=True)
    client = CharField(max_length=101, null=True, blank=True)
    project_date = DateTimeField(auto_now_add=True)
    project_url = URLField()
    category = CharField(max_length=100, null=True, blank=True)
    upload_date = DateTimeField(auto_now_add=True)
    about_project = TextField(null=True, blank=True)


class Blog(Model):
    image = ImageField(null=True, blank=True, upload_to="blog/")
    category = CharField(null=True, blank=True, max_length=100)
    title = CharField(null=True, blank=True, max_length=150)
    text = TextField(null=True, blank=True)
    upload_at = DateTimeField(auto_now_add=True)


class BlogSingle(Model):
    title = CharField(null=True, blank=True, max_length=150)
    text = TextField()
    recent_post = CharField(null=True, blank=True, max_length=150)
    archives = CharField(null=True, blank=True, max_length=150)
    tags = CharField(null=True, blank=True, max_length=150)
    comment = PositiveIntegerField()


class Comment(Model):
    fullname = CharField(max_length=128, blank=True, null=True)
    email = EmailField(max_length=128, blank=True, null=True)
    post_id = ForeignKey("apps.Blog", on_delete=CASCADE)
    text = TextField()
    created_at = DateTimeField(auto_now=True)


class Opinion(Model):
    user = ForeignKey("apps.User", on_delete=CASCADE)
    text = TextField(null=True, blank=True)
