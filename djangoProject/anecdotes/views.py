from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView

import json

from .models import Anecdote
from .serializers import AnecdoteSerializer


class AnecdoteViewSet(viewsets.ModelViewSet):
    queryset = Anecdote.objects.all()
    serializer_class = AnecdoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikePerformViewSet(APIView):
    def post(self, request, pk):
        user_id = request.user.id
        anecdote = Anecdote.objects.get(pk=pk)

        likes_list = json.loads(anecdote.whoLikedIt)
        if user_id in likes_list:
            anecdote.likes -= 1
            likes_list.remove(user_id)
        else:
            anecdote.likes += 1
            likes_list.append(user_id)

        anecdote.whoLikedIt = json.dumps(likes_list)

        anecdote.save()
        return JsonResponse({"status": "OK", "new_likes": anecdote.likes})
