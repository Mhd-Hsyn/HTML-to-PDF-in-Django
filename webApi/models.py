from django.db import models
import uuid
# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(default= uuid.uuid4, editable= False, primary_key=True)
    created_at= models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True)

    class Meta:
        abstract = True

class User(BaseModel):
    fname= models.CharField(max_length=50, null=True, blank=True)
    lname= models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(max_length=254, null=True, blank=True)
    profile= models.ImageField(upload_to="user/", default="user/dummy.png", null=True, blank=True)
    address= models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fname + self.lname
    

class FamilyMember(BaseModel):
    FAMILY_ROLE_CHOICES = [
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('son', 'Son'),
        ('daughter', 'Daughter'),
        ('brother', 'brother'),
        ('sister', 'sister')
    ]
    fname= models.CharField(max_length=50, null=True, blank=True)
    lname= models.CharField(max_length=50, null=True, blank=True)
    family_role= models.CharField(max_length=50, choices= FAMILY_ROLE_CHOICES, null=True, blank=True)
    profession= models.CharField(max_length=50, null=True, blank=True)
    fravorite_food= models.CharField(max_length=50, null=True, blank=True)
    date_of_birth= models.DateField(auto_now=False, auto_now_add=False)
    place_of_birth= models.CharField(max_length=50,  null=True, blank=True)
    lives_in= models.CharField(max_length=50, null=True, blank=True)
    fravorite_holiday= models.CharField(max_length=50, null=True, blank=True)
    greatest_fear= models.CharField(max_length=50, null=True, blank=True)
    quote= models.TextField(null=True, blank=True)
    image= models.ImageField(upload_to="family/", default="user/dummy.png", blank=True, null=True)

    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.fname + self.lname


