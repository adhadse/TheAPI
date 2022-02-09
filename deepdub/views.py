from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView


class SampleView(APIView):
    def get(self, request):
        return JsonResponse({"reply": "hello world"})

    def post(self, request):
        return JsonResponse({"reply": request.data['data']}, status=201)
