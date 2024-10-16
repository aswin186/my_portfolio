from django.db import models
class PersonalDetails(models.Model):
    live = 1
    delete = 0
    profile_status = ((live, 'Live'), (delete, 'Delete'))

    active = models.IntegerField(default=live, choices=profile_status)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    dob = models.DateField()
    email_id = models.CharField(max_length=100)
    mobile_no = models.BigIntegerField()
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/')
    cover_picture = models.ImageField(upload_to='cover_picture/', null=True)
    professional_summary = models.TextField()
    resume = models.FileField(null=True, upload_to='resume/')

    def __str__(self):
        return self.first_name


class Expertise(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    expert_in = models.CharField(max_length=100)

    def __str__(self):
        return self.person_id.first_name + " -- " + self.expert_in


class Skills(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    skills = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.person_id.first_name + " -- " + self.skills


class Languages(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.person_id.first_name + " -- " + self.language_name


class Projects(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    link = models.CharField(null=True, max_length=300)

    def __str__(self):
        return self.person_id.first_name + " -- " + self.project_name


class ProjectTechnologies(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.project.project_name + " -- " + self.technologies


class Education(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    cgpa = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.person_id.first_name + " -- " + self.course_name


class Certificates(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=100)
    uploaded_image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.person_id.first_name + " -- " + self.certificate_name


class MoreDetails(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    hours_worked = models.IntegerField()
    projects_finished = models.IntegerField()
    courses_completed = models.IntegerField()
    workshops_attented = models.IntegerField()

    def __str__(self):
        return self.person_id.first_name


class SocialLinks(models.Model):
    person_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    linkedin = models.CharField(max_length=300)
    github = models.CharField(max_length=300)
    portfolio = models.CharField(null=True, max_length=300)

    def __str__(self):
        return self.person_id.first_name


class NewMessages(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name + " -- " + self.message

