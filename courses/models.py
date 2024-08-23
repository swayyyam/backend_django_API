from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=20,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances')
    year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.course.title} ({self.year}, Semester {self.semester})"
