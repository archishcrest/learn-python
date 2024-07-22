from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from dotenv import load_dotenv
import os
import google.generativeai as genai
# from .rgsetting import stateslistsetting
# from .serializers import ProfileSerializer


load_dotenv()


class TextPromtAndReturn(APIView):

	def post(self, request):

		apiKey = os.getenv("geminiapi")
		genai.configure(api_key=apiKey)

		generation_config = {
			"temperature": 1,
			"top_p": 0.95,
			"top_k": 64,
			"max_output_tokens": 8192,
			"response_mime_type": "text/plain",
		}

		model = genai.GenerativeModel(
			model_name="gemini-1.5-pro",
			generation_config=generation_config,
			# safety_settings = Adjust safety settings
			# See https://ai.google.dev/gemini-api/docs/safety-settings
		)

		chat_session = model.start_chat(
			history=[
			]
		)

		response = chat_session.send_message(request.data['prompt'])
		print(response.text)

		return Response({"message": response.text}, status=status.HTTP_200_OK)
