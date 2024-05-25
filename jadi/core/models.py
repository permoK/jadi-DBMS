from django.db import models



# Create your models here.

class Institution(models.Model):
    institutionId = models.AutoField(primary_key=True, blank=True)
    institutionName = models.CharField(max_length=100, null=True)
    institutionBranch = models.CharField(max_length=100, null=True)
    institutionLocation = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f"{self.institutionName + ' - ' + self.institutionBranch}"


# ################### School #########################
class School(models.Model):
    schoolId = models.AutoField(primary_key=True, blank=True)
    schoolName = models.CharField(max_length=100, null=True)
    # institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    def __str__ (self):
        return self.schoolName + ' - ' + self.institution.institutionName
    
# ################### End School #########################


# ################### Department #########################
class Department(models.Model):
    departmentId = models.AutoField(primary_key=True, blank=True)
    departmentName = models.CharField(max_length=100, null=True)
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return self.departmentName + ' - ' + self.school.schoolName + ' - ' + self.school.institution.institutionName
# ################### End Department #########################

####################student########################
class UserProfile(models.Model):
    ProfileId = models.AutoField(primary_key=True, blank=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    # pfpURL = models.URLField()
    # learningInstitution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    courseMajor = models.CharField(max_length=100)
    # yearOfStudy = models.IntegerField(blank=True, null=True)
    # studentNumber = models.CharField(max_length=100, null=True)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    # interests = models.TextField()
    # savedNotes = models.TextField()
    # likedNotes = models.TextField()
    # following = models.TextField()
    # isCreator = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
    isLecturer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName

################### End student #######################




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

