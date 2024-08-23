from trace import Trace
from django.contrib.auth.models import User
from django.core.serializers import serialize
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Restaurant, Rating
from .serializers import RestaurantSerializer, RatingSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_resto(self, request, pk=None):
        if 'stars' in request.data:

            resto = Restaurant.objects.get(id=pk)
            stars = request.data["stars"]
            user = request.user

            try:
                rating = Rating.objects.get(user=user.id, resto=resto.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {"message": "Rating updated!", 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, resto=resto, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {"message": "Rating received!", 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {"message": "Rating is Required"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {"message": "Unauthorized Route! Please navigate to the ratings page."}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {"message": "Unauthorized Route! Please navigate to the ratings page."}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

