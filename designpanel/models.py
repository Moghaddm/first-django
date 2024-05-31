from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length= 40)
    description = models.CharField(max_length= 100)
    
    def __str__(self) -> str:
        return f"this is quiz of {self.title} with this description: {self.description}"
    
class Question(models.Model):
    text = models.CharField(max_length=300)
    score = models.IntegerField(max_length=100)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"the question is : {self.text}"