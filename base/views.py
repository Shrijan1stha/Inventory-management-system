from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Product, ProductCategory, Department, Suppliers, Purchase
from .serializers import UserSerializer, ProductSerializer, ProductCategorySerializer, DepartmentSerializer, SupplierSerializer, PurchaseSerializer, GroupSerializer
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAuthenticated
from django.contrib.auth.models import Group

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email,password=password)

    if user == None:
        return Response("Invalid credentials")
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def group_listing(request):
    objs = Group.objects.all()
    serializer = GroupSerializer(objs,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        a = serializer.save()
        a.password = hash_password
        a.save()
        return Response('User Created')
    else:
        return Response(serializer.errors)






class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['category', 'department']
    search_fields = ['name', 'description']


class ProductCategoryApiView(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class SupplierApiView(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SupplierSerializer

class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


# Without using </ Model  Viewset \>
class ProductCategoryApiView2(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self,request):
        product_category_obj = self.get_queryset()
        serializer = self.serializer_class(product_category_obj, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DepartmentApiView2(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self,request):
        department_obj = self.get_queryset()
        serializer = self.serializer_class(department_obj, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class SupplierApiView2(GenericAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = SupplierSerializer

    def get(self,request):
        supplier_obj = self.get_queryset()
        serializer = self.serializer_class(supplier_obj,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class PurchaseApiView2(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self,request):
        purchase_obj = self.get_queryset()
        serializer = self.serializer_class(purchase_obj,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)