from django.db import models
import datetime as dt


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["first_name"]


class Category(models.Model):
    choise = models.CharField(max_length=30)

    def __str__(self):
        return self.choise

    class Meta:
        ordering = ["choise"]


class Location(models.Model):
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.area

    class Meta:
        ordering = ["area"]


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pics(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField(max_length=1000)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(default="default.jpg", upload_to="images/")

    def __str__(self):
        return self.title

    @classmethod
    def todays_pics(cls):
        today = dt.date.today()
        bird = cls.objects.filter(pub_date__date=today)
        return bird

    @classmethod
    def days_pics(cls, date):
        bird = cls.objects.filter(pub_date__date=date)
        return bird

    @classmethod
    def search_by_category(cls, search_term):
        bird = cls.objects.filter(category__icontains=search_term)
        return bird
