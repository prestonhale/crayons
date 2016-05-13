  
from voters import phone_validation
from voters.models import Voter, CellCarrier
from voters.serializers import VoterSerializer, CellCarrierSerializer
from markers.generic_permissions import IsOwningUserOrSuperUser
from datetime import datetime
from rest_framework import generics, mixins, status, permissions, viewsets
from rest_framework.response import Response

# Create your views here.
class VoterList(mixins.ListModelMixin,
			    generics.GenericAPIView):
	queryset = Voter.objects.all()
	serializer_class = VoterSerializer
	permission_classes = (permissions.IsAdminUser,)

	def get(self,request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		serializer=serializer_class(request.data)
		if serializer.is_valid():
			user=User.objects.create_user(
				username=request.data['username'],
				password=request.data['password']
				)
			Voter.objects.create(
				user=user,
				phone=request.data['phone'],
				carrier=CellCarrier.objects.get(id=request.data['carrier']),
				)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoterDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Voter.objects.all()
	serializer_class = VoterSerializer
	permission_classes = (permissions.IsAuthenticated,
						IsOwningUserOrSuperUser,)


class CellCarrierViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automaticall provides 'list' and 'detail' actions.
	"""
	queryset = CellCarrier.objects.all()
	serializer_class =  CellCarrierSerializer
	permission_classes = (permissions.IsAuthenticated,)


def validate_phone(request):
	user=User.objects.get(id=request.POST['user_id'])
	voter=Voter.objects.get(user=user)

	key = phone_validation.send_text(voter)

	voter.phone_key = key
	voter.phone_key_generated = datetime.now()
	voter.save()

	return HttpResponse(status=200)