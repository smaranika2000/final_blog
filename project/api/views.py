from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app1.models import Post
from.serializers import PostSerializer
# Create your views here.


@api_view(['GET','POST','PUT','DELETE'])
def post_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Post.objects.get(id = id)
            serializer = PostSerializer(stu)
            return Response(serializer.data)
        stu = Post.objects.all()
        serializer = PostSerializer(stu, many=True) 
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    if request.method == "PUT":
        id = pk
        stu = Post.objects.get(pk = id)
        serializer = PostSerializer(stu, data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Updatesd'})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        id =pk
        stu = Post.objects.get(pk = id)
        stu.delete()
        return Response({'msg':'deleted succcess'})