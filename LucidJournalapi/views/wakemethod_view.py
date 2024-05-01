from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from LucidJournalapi.models import WakeMethod


class WakeMethodView(ViewSet):
    """WakeMethod view set"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            method = WakeMethod.objects.get(pk=pk)
            serializer = WakeMethodSerializer(method)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            methods = WakeMethod.objects.all()
            serializer = WakeMethodSerializer(methods, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)


class WakeMethodSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = WakeMethod
        fields = (
            "id",
            "label",
        )
