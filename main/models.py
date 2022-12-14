from django.db import models

class SkillType(models.Model):
    type_of_skill = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Skill Type'

    def __str__(self):
        return self.type_of_skill

class Skill(models.Model):
    skill = models.CharField(max_length=30)
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.skill


class Degree(models.Model):
    degree = models.CharField(max_length=30)
    organization = models.CharField(max_length=50)
    period = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.degree} {self.period}'

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    
    def __str__(self):
        message = f'A message from {self.name}, {self.email}'
        return message
    

class Dish(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField()
    
    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name    




