from rest_framework.decorators import api_view
from rest_framework.response import Response
from APP.seriallizers import legoserializer, loginserializer
from APP.models import legos
from rest_framework.views import APIView
from rest_framework import viewsets

# Doing CRUD ops inside same tab (just changing the url not the tab!!)

class legolist(APIView):
    def get(self, request):
        serializer = legoserializer(legos.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = legoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def put(self, request):
        serializer = legoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = legos.objects.get(comics=data['comics'])
        serializer = legoserializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        del_comic_name = data['comics']
        if del_comic_name!="/":
            obj = legos.objects.get(comics=del_comic_name)
            obj.delete()
            return Response({"Message": f"{del_comic_name} lego-object is deleted"})
        else:
            legos.objects.all().delete()
            return Response({"Message": "All legos are destroyed"})
            

# Just for doing CRUD ops. in a new tab using ROUTER (After registering in ROUTER)

class legoViewSet(viewsets.ModelViewSet):
    serializer_class = legoserializer
    queryset = legos.objects.all()
    
    def list(self, request):  # Searching by all paramaters (written in models.py) , showing result as a list (JSON format)
        search=request.GET['search']
        comics_query=legos.objects.filter(comics__startswith=search).all()
        serializer=legoserializer(comics_query,many=True)
        if serializer.data !=[]:
            return Response({"Status":"200 Found","data":serializer.data})
        else:
            names_query=legos.objects.filter(names__startswith=search).all()
            serializer=legoserializer(names_query,many=True)
            if serializer.data !=[]:
                return Response({"Status":"200 Found","data":serializer.data})
            else:
                total_query=legos.objects.filter(total__startswith=search).all()
                serializer=legoserializer(total_query,many=True)
                if serializer.data !=[]:
                    return Response({"Status":"200 Found","data":serializer.data})
                else:
                    seller_query=legos.objects.filter(seller__startswith=search).all()
                    serializer=legoserializer(seller_query,many=True)
                    if serializer.data !=[]:
                        return Response({"Status":"200 Found","data":serializer.data})
                    else:
                        return Response({"Status":"203 Not Found"})
                    
                
@api_view(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        data = request.data
        serializer = loginserializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            return Response(serializer.data)

        return Response(serializer.errors)
    else:
        return Response({"Message": "Other Methods are not allowed!!"})