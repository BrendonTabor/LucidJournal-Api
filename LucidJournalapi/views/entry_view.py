from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from LucidJournalapi.models import Entry, WakeMethod, RemCount, DreamFactors
from django.contrib.auth.models import User


class Entryview(ViewSet):
    """game view set"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized instance
        """
        user = request.auth.user

        entry = Entry()
        entry.title = request.data["title"]
        entry.description = request.data["description"]
        entry.user = user
        entry.date_recorded = request.data["date_recorded"]
        entry.wake_method = WakeMethod.objects.get(pk=request.date["wake_method"])
        entry.rem_count = RemCount.objects.get(pk=request.data["rem_count"])

        try:
            entry.save()
            serializer = EntrySerializer(entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(
                {"stupid mortal, malformed object dummy.": ex.args[0]},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item
        Returns:
            Response -- JSON serialized instance
        """
        try:
            entry = Entry.objects.get(pk=pk)
            serializer = EntrySerializer(entry)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            entry = Entry.objects.get(pk=pk)
            entry.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Entry.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response(
                {"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def list(self, request):
        """Handle GET requests for all items
        Returns:
            Response -- JSON serialized array
        """
        try:
            entry = Entry.objects.all()
            serializer = EntrySerializer(entry, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)


class UserEntrySerializer(serializers.ModelSerializer):

    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    """JSON Serializer"""

    class Meta:
        model = User
        fields = (
            "id",
            "firstName",
            "lastName",
            "username",
        )


class WakeMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = WakeMethod
        fields = (
            "id",
            "label",
        )


class RemCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemCount
        fields = ("id", "cycles_completed")


class EntrySerializer(serializers.ModelSerializer):
    """JSON Serializer"""

    user = UserEntrySerializer(many=False)
    dateRecorded = serializers.DateField(source="date_recorded")
    wake_method = WakeMethodSerializer(many=False)
    rem_count = RemCountSerializer(many=False)

    class Meta:
        model = Entry
        fields = (
            "id",
            "title",
            "description",
            "dateRecorded",
            "user",
            "wake_method",
            "rem_count",
        )
