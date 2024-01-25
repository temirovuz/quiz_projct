from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class QuizType(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='quiztype/', null=True, blank=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(QuizType, on_delete=models.CASCADE)
    name = models.TextField()

    def is_right_answer(self, pk):
        return self.answers.filter(pk=pk, is_right=True).exists()

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    name = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    total_question = models.IntegerField()
    corrent_question = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(QuizType, on_delete=models.CASCADE)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.total = round((100 * self.corrent_question) / self.total_question, 2)
        return super().save(*args, **kwargs)