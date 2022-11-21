from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,request
from .serializers import *

class ProductPrices(APIView):
    def get(self,resquest):
        model = Pricing.objects.all()
        serializer = PricingSerializer(model, many=True)
        return Response(serializer.data)

    def post(self,resquest):
        product_id = request.data.get('id')
        product_distance = request.data.get('distance')
        product_time = request.data.get('time_taken')
        total_price = request.data.get('total_price')
        serializer = PricingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # try:
            #     if product_id is not None:
            #         if product_distance < 3:
            #             total_price = 80
            #         elif product_distance > 3 and product_distance<= 3.5:
            #             total_price = 90
            #         else product_distance 
            
            # except:
            #         return Response('product with id does not exists')
            return Response(serializer.data(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id):
        if not self.get(id):
            return Response(f'Product id {id} does not exist in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)