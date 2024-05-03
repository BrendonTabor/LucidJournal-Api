from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from LucidJournalapi.models import SleepFactor


class SleepFactorView(ViewSet):
    """Category view set"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            sleepfactor = SleepFactor.objects.get(pk=pk)
            serializer = SleepFactorSerializer(sleepfactor)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            sleepfactors = SleepFactor.objects.all()
            serializer = SleepFactorSerializer(sleepfactors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)


class SleepFactorSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = SleepFactor
        fields = (
            "id",
            "label",
        )
