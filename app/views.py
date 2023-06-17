from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import APIView,permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
class product(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PJD=Proms(PQS,many=True)
        return Response(PJD.data)
    def post(self,request,id):
        PMSD=Proms(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'POST':'Created successfully'})
        return Response({'POST':'Creation failed'})
    def put(self,request,id):
        PO=request.data['id']
        PQS=Product.objects.get(id=PO)
        PMSD=Proms(PQS,data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'PUT':'Updation is successfull'})
        return Response({'PUT':'Updation is failed'})
    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PO.Pname=request.data['Pname']
        PO.save()
        return Response({'PATCH':'partial updation is successfull'})
    
    def delete(self,request,id):
       Product.objects.get(id=id).delete()
       return Response({'delete':'deleted successfully'})

