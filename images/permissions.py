from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        print("*" * 200)
        return obj.author == request.user
