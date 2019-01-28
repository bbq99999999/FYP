from django.db import models


# Create your models here.
class MyUser(models.Model):
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=50)
    birth = models.DateField(null=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    phone = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Feedback(models.Model):
    email = models.EmailField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=50, null=False, unique=True)
    company = models.TextField(max_length=50)
    content = models.TextField(max_length=1000)

    def __repr__(self):
        return self.email


class Continent(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Activities(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    price = models.FloatField(null=False)
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __repr__(self):
        return self.title


class Exchange(models.Model):
    price = models.FloatField
    currency = models.FloatField
    payment = models.CharField(max_length=20)

    def __repr__(self):
        return self.price


class FAQ(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=200)

    def __repr__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.ForeignKey('Continent', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, null=False)
    continent = models.ForeignKey('Continent', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    rating = models.ForeignKey('Rating', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)
    activities = models.ForeignKey('Activities', null=False, on_delete=models.CASCADE)

    def __repr__(self):
        return self.title


class Rating(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=300)
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)

    def __repr__(self):
        return self.title


class Flight(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateField
    company = models.ForeignKey('Company', null=False, on_delete=models.CASCADE)
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.TextField(max_length=50)
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    price = models.IntegerField
    quantity = models.IntegerField
    payment = models.CharField(max_length=20)
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)

    def __repr__(self):
        return self.price


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField
    type = models.CharField(max_length=20)
    price = models.FloatField
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Discount(models.Model):
    percentage = models.FloatField
    hotel = models.ForeignKey('Hotel', null=False, on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', null=False,
                               on_delete=models.CASCADE)

    def __repr__(self):
        return self.percentage


class Weather(models.Model):
    name = models.CharField(max_length=20)
    time = models.DateField
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Culture(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Booking(models.Model):
    quantity = models.IntegerField
    check_in_date = models.DateField
    check_out_date = models.DateField
    hotel = models.ForeignKey('Hotel', null=False, on_delete=models.CASCADE)
    invoice = models.ForeignKey('Invoice', null=False, on_delete=models.CASCADE)
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)


class FlightTicket(models.Model):
    quantity = models.IntegerField
    check_in_date = models.DateField
    check_out_date = models.DateField
    flight = models.ForeignKey('Flight', null=False, on_delete=models.CASCADE)
    invoice = models.ForeignKey('Invoice', null=False, on_delete=models.CASCADE)
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)


class CateGory(models.Model):
    group_title = models.CharField(max_length=20)
    forum_place = models.ForeignKey('ForumPlace', null=False,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.group_title


class ForumPlace(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=20)
    post_date = models.DateTimeField
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)
    category = models.ForeignKey('CateGory', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    date = models.DateField
    place = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ShopHistory(models.Model):
    data = models.DateField
    invoice = models.ForeignKey("Invoice", null=False, on_delete=models.CASCADE)
    user = models.ForeignKey("MyUser", null=False, on_delete=models.CASCADE)

    def __repr__(self):
        return self.invoice


class LoginHistory(models.Model):
    data = models.DateField
    user = models.ForeignKey('MyUser', null=False, on_delete=models.CASCADE)

    def __repr__(self):
        return self.data


class Themes(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField
    place = models.ForeignKey("Place", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.TextField
    data = models.DateField
    views = models.IntegerField
    content = models.TextField
    user = models.ForeignKey("MyUser", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField
    activities = models.ForeignKey('Activities', null=False, on_delete=models.CASCADE)
    themes = models.ForeignKey('Themes', null=False, on_delete=models.CASCADE)
    place = models.ForeignKey("Place", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name


class Function(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name


class Benefit(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name


class EmployeeHistory(models.Model):
    department = models.ForeignKey('Department', null=False, on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', null=False, on_delete=models.CASCADE)
    begin_date = models.DateField(auto_now=True, null=True)
    end_date = models.DateField


class Employee(models.Model):
    full_name = models.CharField(max_length=150, null=False)
    address = models.TextField(max_length=50, null=False)
    fiscal_number = models.IntegerField(null=False)
    employee_number = models.IntegerField(null=False)
    department = models.ForeignKey('Department', null=False, on_delete=models.CASCADE)
    function = models.ForeignKey('Function', null=False, on_delete=models.CASCADE)
    benefits = models.ForeignKey('Benefit', null=False, on_delete=models.CASCADE)
    begin_date = models.DateField(auto_now=True, null=True)
    end_date = models.DateField(auto_now=True, null=True)

    def __repr__(self):
        return self.full_name


class Register(models.Model):
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=50)
    birth = models.DateField
    email = models.EmailField(max_length=100, null=False, unique=True)
    phone = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)

    def __str__(self):
        return self.username
