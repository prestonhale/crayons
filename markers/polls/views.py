from rest_framework import generics, permissions
from polls.models import Poll, PollResponse, PollChoice
from polls.serializers import PollSerializer, PollResponseSerializer, PollChoiceSerializer
from markers.generic_permissions import IsOwningUserOrSuperUser


class PollList(generics.ListCreateAPIView):
    queryset=Poll.objects.all()
    serializer_class=PollSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PollChoiceList(generics.ListCreateAPIView):
    queryset = PollChoice.objects.all()
    serializer_class = PollChoiceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PollResponseList(generics.ListCreateAPIView):
    queryset = PollResponse.objects.all()
    serializer_class = PollResponseSerializer
    permission_classes = (permissions.IsAdminUser,)


class PollResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollResponse.objects.all()
    serializer_class = PollResponseSerializer
    permission_classes = (IsOwningUserOrSuperUser,)

