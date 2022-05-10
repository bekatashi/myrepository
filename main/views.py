from rest_framework import generics, permissions
from main.serializers import *
from rest_auth import views


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer


class CustomLogOutView(views.LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class ProductsView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductsDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

