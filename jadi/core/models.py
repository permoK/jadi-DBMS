from django.db import models



# Create your models here.

class UserProfile(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    pfpURL = models.URLField()
    learningInstitution = models.CharField(max_length=100)
    courseMajor = models.CharField(max_length=100)
    interests = models.TextField()
    savedNotes = models.TextField()
    likedNotes = models.TextField()
    following = models.TextField()
    isCreator = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName


class Note(models.Model):
    noteid = models.AutoField(primary_key=True)
    noteName = models.CharField(max_length=100)
    noteDescription = models.TextField()
    noteURL = models.URLField()
    extension = models.CharField(max_length=10)
    size = models.IntegerField()
    cmsId = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    tags = models.TextField()
    category = models.CharField(max_length=100)
    views = models.IntegerField()
    popularity = models.IntegerField()
    saves = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self):
        return self.noteName

class savedNotes(models.Model):
    noteid = models.AutoField(primary_key=True)
    noteName = models.CharField(max_length=100)
    noteDescription = models.TextField()
    noteURL = models.URLField()
    extension = models.CharField(max_length=10)
    size = models.IntegerField()
    cmsId = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    tags = models.TextField()
    category = models.CharField(max_length=100)
    views = models.IntegerField()
    popularity = models.IntegerField()
    saves = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self):
        return self.noteName



# class Comment(models.Model):
#     commentid = models.AutoField(primary_key=True)
#     noteid = models.ForeignKey(Note, on_delete=models.CASCADE)
#     userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     comment = models.TextField()
#     createdAt = models.DateTimeField(auto_now_add=True)
#     updatedAt = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.comment
