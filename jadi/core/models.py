from django.db import models



# Create your models here.

####################student########################
class UserProfile(models.Model):
    ProfileId = models.AutoField(primary_key=True, blank=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    # pfpURL = models.URLField()
    learningInstitution = models.CharField(max_length=100)
    courseMajor = models.CharField(max_length=100)
    # interests = models.TextField()
    # savedNotes = models.TextField()
    # likedNotes = models.TextField()
    # following = models.TextField()
    isCreator = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
    isLecturer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName

################### End student #######################

# ################### School #########################
class School(models.Model):
    schoolId = models.AutoField(primary_key=True, blank=True)
    schoolName = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return self.schoolName
    
# ################### End School #########################


# ################### Department #########################
class Department(models.Model):
    departmentId = models.AutoField(primary_key=True, blank=True)
    departmentName = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.departmentName
# ################### End Department #########################


# ################## Lecturer ##########################
# class Lecturer(models.Model):
#     lecturerId = models.AutoField(primary_key=True)
#     lFirstName = models.CharField(max_length=100, null=True)
#     lLastName = models.CharField(max_length=100)
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.lFirstName + ' ' + self.lLastName


# ################## End Lecturers ##########################



# ################### Notes ###############################

# class ResourceCategory(models.Model):
#     resourceId = models.AutoField(primary_key=True)
#     resourceName = models.CharField(max_length=100)
#     resourceDescription = models.TextField()
#     def __str__(self):
#         return self.resourceName


# class AcademicResource(models.Model):
#     # AcademicResourceId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     AcademicResourceId = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     resource = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
#     uploadedBy = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='uploadedBy')

#     def __str__(self):
#         return self.name



# ################## End Notes ################################


# ################## Authorized uploaders #################################

# class AuthorizedUploader(models.Model):
#     uploaderId = models.AutoField(primary_key=True)
#     name = models.ManyToManyField(UserProfile or Lecturer)

# ################## End Authorized uploaders ##############################

# ################# comments #################################

# # class Comment(models.Model):
# #     commentid = models.AutoField(primary_key=True)
# #     noteid = models.ForeignKey(Note, on_delete=models.CASCADE)
# #     userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
# #     comment = models.TextField()
# #     createdAt = models.DateTimeField(auto_now_add=True)
# #     updatedAt = models.DateTimeField(auto_now=True)

# #     def __str__(self):
# #         return self.comment

# ################### End comments ############################

