from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import serializers
from rest_framework.decorators import APIView
from rest_framework.response import Response


from .models import Certificate


class CertificatePDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['jshshr', 'course']
        
from django.urls import reverse

class CertificatePDFView(APIView):
    serializer_class = CertificatePDFSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        serializer = self.serializer_class(data=request.GET)
        if serializer.is_valid():
            jshshr = serializer.validated_data['jshshr']
            course = serializer.validated_data['course']
            pdf_file = Certificate.objects.filter(jshshr=jshshr, course=course).first()
            if pdf_file:
                return Response({'pdf_url': "https:ejournal.uzbmb.uz/malaka/pdfs/" + pdf_file.hash})
            else:
                return Response({'error': 'PDF not found'}, status=404)
        else:
            return Response(serializer.errors, status=400)