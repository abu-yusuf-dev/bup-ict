from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    image = models.ImageField(upload_to='Events/')

    def __str__(self):
        return self.name

class Documents(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='Documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Admission(models.Model):
    program_name = models.CharField(max_length=50)
    link = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


    def __str__(self):
        return self.program_name

class Curriculum(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    room_no = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='Faculty/')
    research_interest = models.CharField(max_length=50)
    courses = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Staff/')

    def __str__(self):
        return self.name

class ResearchGroup(models.Model):
    name = models.CharField(max_length=50)
    members = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    research_area = models.CharField(max_length=50)
    current_work = models.CharField(max_length=50)
    publications = models.CharField(max_length=50)
    resources = models.CharField(max_length=50)
    photo_gallery = models.ImageField(upload_to='Research_Group/')
    notice = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Notice(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='Notice/')

    def __str__(self):
        return self.name

class HonorBoard(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Honor_Board/')

    def __str__(self):
        return self.name

class Alumni(models.Model):
    event_name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='Alumni/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name






