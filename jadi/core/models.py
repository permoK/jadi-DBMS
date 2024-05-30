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
# class UserProfile(models.Model):
#     profileId = models.AutoField(primary_key=True, blank=True)
#     clerkId = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     fullName = models.CharField(max_length=100)
#     email = models.EmailField(max_length=256)
#     learningInstitution = models.ForeignKey('LearningInstitution', on_delete=models.CASCADE, blank=True, null=True)
#     courseMajor = models.CharField(max_length=100, blank=True)
#     interests = models.ManyToManyField(Interest)
#     customUserInterest = ArrayField(models.CharField(max_length=100), blank=True, null=True)
#     isStudent = models.BooleanField()
#     isLecturer = models.BooleanField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'userprofile'

#     def __str__(self):
#         return self.fullName

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clerk_id = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username

#################### End User ##############################


#################### Course ##############################
class Major(models.Model):
    major_name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'major'

    def __str__(self):
        return self.major_name
#################### End Course ##############################

#################### UserEducationDetails ##############################
class UserEducationDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_institution = models.ForeignKey(LearningInstitution, on_delete=models.CASCADE)
    student_major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True)
    units = models.JSONField()

    class Meta:
        db_table = 'user_education_details'

    def __str__(self):
        return f'{self.user.username} - {self.learning_institution.institution_name}'

#################### End UserEducationDetails ##############################
