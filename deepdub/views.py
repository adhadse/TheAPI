from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser


class SampleView(APIView):
    def get(self, request):
        return JsonResponse({"reply": "hello world"})

    def post(self, request):
        return JsonResponse({"reply": request.data['data']}, status=status.HTTP_201_CREATED)


def deepdub_redirect(request):
    return HttpResponseRedirect(redirect_to='https://developer.anuragdhadse.com/deepdub')
