from django.db import models
from django.contrib.auth.models import User
# from user_profile.models import UserProfile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name

class Plant(models.Model):
    title = models.CharField(max_length = 50)
    price = models.DecimalField(null=True, blank=True,default=4.99,max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete = models.CASCADE, default=1,blank=True, null=True)
    # category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    # image = models.ImageField(upload_to="plants/images/")
    image = models.URLField(blank=True, null=True)
    description = models.TextField()
    quantity = models.IntegerField(default=1, null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    sold = models.IntegerField(default=0, null=True, blank=True)
    
    # def __str__(self):
    #     return f"{self.title} of Mr. {self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE)
    Plant = models.ForeignKey(Plant, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"User : {self.reviewer.user.first_name} ; Plant: {self.Plant.user.first_name}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.Plant.title}"