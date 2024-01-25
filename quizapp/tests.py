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


class TestHelloWord(TestCase):
    def setUp(self) -> None:
        self.url = reverse('hello_world')

    def test_gets(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert response.json()['message'] == 'hello world'


class TestQuizTypeView(TestCase):
    def setUp(self):
        self.quiz_type1 = QuizType.objects.create(name='Test 1')
        self.quiz_type2 = QuizType.objects.create(name='Test 2')

        self.url = reverse('quiz_types')

    def test_get(self):
        quiz_types = QuizType.objects.all()
        serializers = QuizTypeSerializer(quiz_types, many=True)

        response = self.client.get(self.url)

        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_post_is_vaild(self):
        pyload = {
            'name': 'Test',
            'image': ""
        }

        response = self.client.post(self.url, data=pyload)

        assert response.status_code == 201

    def test_post_is_invaild(self):
        pyload = {
            'names': 'Test',
            'image': ""
        }

        response = self.client.post(self.url, data=pyload)

        assert response.status_code == 400

