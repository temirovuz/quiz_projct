from rest_framework import serializers

from quizapp.models import QuizType, Question, Answer, Result


class QuizTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizType
        fields = ['name','image']

    def validate(self, data):
        if len(data['name']) <= 2:
            raise serializers.ValidationError('Kammida 3 ta belgi bulish kerak')
        return data

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['count_question'] = instance.question_set.count()
        return res


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['name', 'is_right']

class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizTypeSerializer(read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['pk', 'name', 'quiz', 'answers']

    def get_answers(self, obj):
        serializers = AnswerSerializer(obj.answers.all(), many=True)
        return serializers.data

    def to_representation(self, instance):
        res = super().to_representation(instance)
        request = self.context.get('request')
        print(self.context, 'context')
        if request:
            res['username'] = request.user.username
        return res


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"