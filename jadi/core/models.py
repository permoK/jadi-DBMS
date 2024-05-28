from django.db import models
from django.contrib.postgres.fields import ArrayField



# Create your models here.

#################### LearningInstitution ##############################
class LearningInstitution(models.Model):
    institutionId = models.AutoField(primary_key=True, blank=True)
    institutionName = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'learninginstitution'

    def __str__(self):
        return self.institutionName
#################### End LearningInstitution ##############################

#################### Interests ##############################
class Interest(models.Model):
    interestId = models.AutoField(primary_key=True)
    interestName = models.CharField(max_length=100)

    class Meta:
        db_table = 'interests'

    def __str__(self):
        return self.interestName
#################### End Interests ##############################

#################### User ##############################
class UserProfile(models.Model):
    profileId = models.AutoField(primary_key=True, blank=True)
    clerkId = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    learningInstitution = models.ForeignKey('LearningInstitution', on_delete=models.CASCADE, blank=True, null=True)
    courseMajor = models.CharField(max_length=100, blank=True)
    interests = models.ManyToManyField(Interest)
    customUserInterest = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    isStudent = models.BooleanField()
    isLecturer = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'userprofile'

    def __str__(self):
        return self.fullName


#################### End User ##############################


## ################### School #########################
#class School(models.Model):
#    schoolId = models.AutoField(primary_key=True, blank=True)
#    schoolName = models.CharField(max_length=100, null=True)
#    # institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
#    def __str__ (self):
#        return self.schoolName + ' - ' + self.institution.institutionName
    
## ################### End School #########################


## ################### Department #########################
#class Department(models.Model):
#    departmentId = models.AutoField(primary_key=True, blank=True)
#    departmentName = models.CharField(max_length=100, null=True)
#    # school = models.ForeignKey(School, on_delete=models.CASCADE)
#    def __str__(self):
#        return self.departmentName + ' - ' + self.school.schoolName + ' - ' + self.school.institution.institutionName
## ################### End Department #########################

#####################student########################
## class UserProfile(models.Model):
##     ProfileId = models.AutoField(primary_key=True, blank=True)
##     fullName = models.CharField(max_length=100)
##     email = models.EmailField()
##     # pfpURL = models.URLField()
##     # learningInstitution = models.ForeignKey(Institution, on_delete=models.CASCADE)
##     courseMajor = models.CharField(max_length=100)
##     # yearOfStudy = models.IntegerField(blank=True, null=True)
##     # studentNumber = models.CharField(max_length=100, null=True)
##     # department = models.ForeignKey(Department, on_delete=models.CASCADE)
##     # school = models.ForeignKey(School, on_delete=models.CASCADE)
##     # interests = models.TextField()
##     # savedNotes = models.TextField()
##     # likedNotes = models.TextField()
##     # following = models.TextField()
##     # isCreator = models.BooleanField(default=False)
##     isStudent = models.BooleanField(default=False)
##     isLecturer = models.BooleanField(default=False)
##     created_at = models.DateTimeField(auto_now_add=True)
##     updated_at = models.DateTimeField(auto_now=True)

##     def __str__(self):
##         return self.fullName

#################### End student #######################
## ################## Lecturer ##########################
## class Lecturer(models.Model):
##     lecturerId = models.AutoField(primary_key=True)
##     lFirstName = models.CharField(max_length=100, null=True)
##     lLastName = models.CharField(max_length=100)
##     school = models.ForeignKey(School, on_delete=models.CASCADE)
##     Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
##     def __str__(self):
##         return self.lFirstName + ' ' + self.lLastName


## ################## End Lecturers ##########################



## ################### Notes ###############################

## class ResourceCategory(models.Model):
##     resourceId = models.AutoField(primary_key=True)
##     resourceName = models.CharField(max_length=100)
##     resourceDescription = models.TextField()
##     def __str__(self):
##         return self.resourceName


## class AcademicResource(models.Model):
##     # AcademicResourceId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
##     AcademicResourceId = models.AutoField(primary_key=True)
##     name = models.CharField(max_length=100)
##     description = models.TextField()
##     resource = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
##     uploadedBy = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='uploadedBy')

##     def __str__(self):
##         return self.name



## ################## End Notes ################################


## ################## Authorized uploaders #################################

## class AuthorizedUploader(models.Model):
##     uploaderId = models.AutoField(primary_key=True)
##     name = models.ManyToManyField(UserProfile or Lecturer)

## ################## End Authorized uploaders ##############################

## ################# comments #################################

## # class Comment(models.Model):
## #     commentid = models.AutoField(primary_key=True)
## #     noteid = models.ForeignKey(Note, on_delete=models.CASCADE)
## #     userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
## #     comment = models.TextField()
## #     createdAt = models.DateTimeField(auto_now_add=True)
## #     updatedAt = models.DateTimeField(auto_now=True)

## #     def __str__(self):
## #         return self.comment

## ################### End comments ############################

