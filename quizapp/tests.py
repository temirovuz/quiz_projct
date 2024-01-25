from django.test import TestCase
from django.urls import reverse

from quizapp.api.v1.serializers import QuizTypeSerializer
from quizapp.models import QuizType


class TestQuizTypeSerializer(TestCase):
    def setUp(self):
        self.quiz_type = QuizType.objects.create(name='Test quiz type')

    def test_data(self):
        serializer = QuizTypeSerializer(self.quiz_type).data

        assert serializer['id'] == self.quiz_type.id


class TestQuizTypeSerializer(TestCase):
    def setUp(self):
        self.quiz_type = QuizType.objects.create(name='Test quiz type')

    def test_data(self):
        serializer = QuizTypeSerializer(self.quiz_type).data

        assert serializer['id'] == self.quiz_type.id


class TestQuizTypeView(TestCase):
    def setUp(self):
        self.quiz_type1 = QuizType.objects.create(name='Test 1')
        self.quiz_type2 = QuizType.objects.create(name='Test 2')

        self.url = reverse('qiuz')

    def test_get(self):
        quiz_types = QuizType.objects.all()
        serializers = QuizTypeSerializer(quiz_types, many=True)

        response = self.client.get(self.url)

        assert response.status_code == 200




