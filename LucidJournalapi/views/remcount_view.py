from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from LucidJournalapi.models import RemCount


class RemCountView(ViewSet):
    """WakeMethod view set"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            count = RemCount.objects.get(pk=pk)
            serializer = RemCountSerializer(count)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            counts = RemCount.objects.all()
            serializer = RemCountSerializer(counts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)


class RemCountSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = RemCount
        fields = (
            "id",
            "label",
        )
