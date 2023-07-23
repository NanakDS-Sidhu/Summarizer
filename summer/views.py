from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import SummerNews

# Create your views here.
class SummerView(APIView):
    def get(self,request):
        url=request.query_params['url']
        if not url:
            return Response(f"Empty url",status=500)

        out=SummerNews.extract_text(url)
        return Response(out,status=200)

