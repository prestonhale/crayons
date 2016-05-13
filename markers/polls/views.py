from rest_framework import generics, permissions
from polls.models import Poll
from polls.serializers import PollSerializer


class PollList(generics.ListCreateAPIView):
	queryset=Poll.objects.all()
	serializer_class=PollSerializer
	permission_classes = (permissions.IsAuthenticated,)


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer
	permission_classes = (permissions.IsAuthenticated,)