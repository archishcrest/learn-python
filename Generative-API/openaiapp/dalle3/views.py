from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
import os
from openai import OpenAI  # OpenAI Python library to make API calls
#import requests  # used to download images
from PIL import Image  # used to print and edit images

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class generateImage(APIView):
    def get(self, request):

    	response = client.images.generate(
    		model="dall-e-3",
    		prompt="a white siamese cat",
    		size="1024x1024",
    		quality="standard",
    		n=1,
    		)

    	return Response({"response": response}, status=status.HTTP_200_OK)