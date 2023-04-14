from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import GenericViewSet

from .models import Certificate


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['pdf_certificate']


class CertificateAPIView(mixins.ListModelMixin, GenericViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jshshr', 'course']
    permission_classes = [IsAdminUser]
