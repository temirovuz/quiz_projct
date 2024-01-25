from django.core.cache import cache

from quizapp.models import Result


def check_answer(request):
    questions = cache.get('questions')
    correct = 0
    wrong = 0

    for q in questions:
        if q.is_right_answer(request.POST.get(q.name)):
            correct += 1
        else:
            wrong += 1
        quiz = q.quiz
    Result.objects.create(
        user=request.user,
        total_question=len(questions),
        corrent_question=correct,
        quiz=quiz
    )
    context = {
        'correct': correct,
        'wrong': wrong,
        'total_question': len(questions),
        'user': request.user.username,
        'total': round(correct * 100 / len(questions), 2)
    }
    return context