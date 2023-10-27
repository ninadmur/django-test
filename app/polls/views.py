from .models import Question,Choice
from .serializers import QuestionSerializer,ChoiceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class QuestionList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class QuestionDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
 
class ChoiceList(APIView):
    def get(self, request, format=None):
        choices = Question.objects.all()
        serializer = QuestionSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChoiceByQuestion(APIView):
    def get(self, request, question_id, format=None):
        try:
            question = Question.objects.get(pk=question_id)
            print(question)
        except Question.DoesNotExist:
            raise Http404

        choices = Choice.objects.filter(question=question_id)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)
    


class ChoiceDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
 