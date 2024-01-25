from django.test import TestCase
from django.urls import reverse

from quizapp.api.v1.serializers import QuizTypeSerializer
from quizapp.models import QuizType


class TestQuizType(TestCase):
    def setUp(self):
        self.quiz_type = QuizType.objects.creat(name='Test quiz type')

    def test_data(self):
        serializers = QuizTypeSerializer(self.quiz_type).data

        assert serializers['id'] == self.quiz_type.id


class HelloWorld(TestCase):
    def setUp(self):
        self.url = reverse('hello world')

    def test_gets(self):
        respomse = self.client.get(self.url)
        assert respomse.status_code == 200
        assert respomse.json()['message'] == 'hello world'
