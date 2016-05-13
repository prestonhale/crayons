from rest_framework import permissions


class IsUser(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def had_object_permissions(self, request, view, obj):
		# Superuser can interact with all users
		if request.is_superuser:
			return True
		# Other users can only interact with themselves
		return obj.user == request.user