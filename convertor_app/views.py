
from rest_framework.views import APIView
from convertor_app import utils
from rest_framework.response import Response

from convertor_app.serializer import ConvertToNumberSerializer, ConvertToWordSerializer

class ConvertToNumberView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = ConvertToNumberSerializer(data=request.data)
            if serializer.is_valid():
                
                words = serializer.data['words']
                number = utils.words_to_number(words)
                response_data = {'number': number}
                return Response(response_data, status=200)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            error_message = {'error': str(e)}
            return Response(error_message, status=422)

   

class ConvertToWordView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = ConvertToWordSerializer(data=request.data)
            if serializer.is_valid():
                
                number = serializer.data['number']
                words = utils.number_to_words(number)
                response_data = {'words': words}
                return Response(response_data, status=200)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            error_message = {'error': str(e)}
            return Response(error_message, status=422)

   
