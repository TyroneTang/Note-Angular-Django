from notes.models import Note
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, NoteSerializer, NoteDisplaySerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from Crypto.Cipher import AES
import binascii, os

# Create your views here.


def index(request):
    return render(request, 'notes/index.html')

# =================================== API REQUESTS =====================================
@api_view(['GET', 'POST'])
@csrf_exempt
def notes(request,id):
    
    if request.method == 'POST':
        data = request.data
        user = User.objects.get(pk=id)
        note = Note(
            user=user,
            title=data["title"], 
            note=data["note"]
        )
        note.save()
        return JsonResponse({"message" : "Data saved"}, status=200)
    else:
        
        note = Note.objects.filter(user=id)
        serialize = NoteDisplaySerializer(note, many=True)       
        return Response(serialize.data)
    
@api_view(['GET', 'PUT'])
@csrf_exempt
def edit_notes(request,id):
   
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
        
    if request.method == 'PUT':
        serialize = NoteSerializer(instance=note, data = request.data)
        if serialize.is_valid():
            serialize.save()
        else:
            return Response (serialize.errors)

    serialize = NoteDisplaySerializer(note)
    return Response(serialize.data)

@api_view(['GET', 'DELETE'])
@csrf_exempt
def delete_notes(request, id):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        note.delete()
        
    return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)  

# ======================================= ENCRYPTION & DECRYPTION ===============================

# secretKey = os.urandom(32)
# print("Encryption key:", binascii.hexlify(secretKey))
# msg = b'Message for AES-256-GCM + Scrypt encryption'


# def encrypt_AES_GCM(item, secretKey):
#     aesCipher = AES.new(secretKey, AES.MODE_GCM)
#     ciphertext, authTag = aesCipher.encrypt_and_digest(item)
#     return (ciphertext, aesCipher.nonce, authTag)


# def decrypt_AES_GCM(encryptedItem, secretKey):
#     (ciphertext, nonce, authTag) = encryptedItem
#     aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
#     plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
#     return plaintext





# encryptedMsg = encrypt_AES_GCM(msg, secretKey)
# print("encryptedMsg", {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'aesIV': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2])
# })

# decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
# print("decryptedMsg", decryptedMsg)
