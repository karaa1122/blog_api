from django.db import models
import uuid
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Tags(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=50)




class Basemodel(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract = True



class Blog(Basemodel):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title=models.CharField(max_length=200)
    blog_text=models.TextField()
    tag=models.ManyToManyField(Tags)
    image=models.ImageField(upload_to="blogs")

    def __str__(self) -> str:
        return self.title


class Comment(MPTTModel):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['created_at']

    def __str__(self):
        return self.content
class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
