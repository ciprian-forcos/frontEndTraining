from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import Note
from .serializers import NoteSerializer
from rest_framework import status
from .request import createNoteRequest 
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# # Create your views here.
# @api_view(["GET"])
# def getNotes(request):
#     try:    
#         notes = Note.objects.all()
#         arrayList = NoteSerializer(notes,many = True)
#         return Response(arrayList.data)
#     except Note.DoesNotExist:
#         return Response("Notes not available")
#     except Exception as e:
#         print(e)
#         return Response("Internal Server Error")
    
# @api_view(["GET"])
# def getNote(request, pk):
#     try:
#         note = Note.objects.get(id = pk)
#         serializer = NoteSerializer(note, many=False)
#         return Response(serializer.data)
#     except Note.DoesNotExist:
#         return Response("Note not available")
#     except Exception as e:
#         print(e)
#         return Response("Internal Server Error")
    

class NOTE_VIEW_WITHOUT_PK(APIView):
    def get(self, request):
        try:
            note = Note.objects.all()
            notesList = NoteSerializer(note, many=True)
            return Response({"data":notesList.data},status=status.HTTP_200_OK)
        
        except Note.DoesNotExist:
            return Response({"data":"No Notes exist!"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"data": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
       request_body=createNoteRequest 
    )       
    def post(self, request):
        try:
            data = request.data
            name = data["name"]
            description = data["description"] 
            Note.objects.create(name = name, description = description)
            return Response({"data": "Success"}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
            return Response({"data": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(selt, request):
        try:
            pass
        exce