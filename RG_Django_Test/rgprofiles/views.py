from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.db.models import F
from .models import *
import json
from collections import defaultdict
from django.db.models import Count
from dotenv import load_dotenv
import os
from .rgsetting import stateslistsetting

load_dotenv()

class BusinessByCategory(APIView):
    def get(self, request):
    	
    	states = os.getenv("allowed_states").split(",")

    	categories = ProfileCategory.objects.filter(
    		profilecategorylocation__state__in=states
    		).select_related('category_id').distinct().order_by('name').values('name', 'slug')

    	if categories.exists():

    		grouped_data = defaultdict(list)

	    	# Sort categories alphabetically by 'name'
	    	sorted_categories = sorted(list(categories), key=lambda x: x['name'])

	    	for category in sorted_categories:
	    		first_letter = category['name'][0].upper()
	    		grouped_data[first_letter].append({
	    			"name": category["name"],
	    			"slug": category["slug"]
	    		})

	    	# Convert defaultdict to regular dictionary for JSON serialization
	    	output_data = dict(grouped_data)

	    	return Response({"business": output_data}, status=status.HTTP_200_OK)
    	else:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)



class BusinessByCategoryState(APIView):
    def get(self, request, state=None):

    	states = os.getenv("allowed_states").split(",")

    	if state.upper() not in states:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)

    	stateIn = [stateslistsetting[state.upper()],state.upper()]

    	categories = ProfileCategoryLocation.objects.select_related('category_id') \
    	.filter(state__in=stateIn).values('category_id__name', 'category_id__slug', 'city') \
    	.annotate(category_id__name_count=Count('category_id__name'))

    	#print(categories.query)

    	if categories.exists():

    		grouped_data = defaultdict(list)
    		city_data = []
    		temt_name = []

	    	# Sort categories alphabetically by 'name'
	    	sorted_categories = sorted(list(categories), key=lambda x: x['category_id__name'])

	    	for category in sorted_categories:
	    		first_letter = category['category_id__name'][0].upper()

	    		if category["category_id__name"] not in temt_name:
	    			temt_name.append(category["category_id__name"])
	    			grouped_data[first_letter].append({
		    			"name": category["category_id__name"],
		    			"slug": category["category_id__slug"]
		    		})

	    		if category["city"] not in city_data:
	    			city_data.append(category["city"])

	    	# Convert defaultdict to regular dictionary for JSON serialization
	    	output_data = dict(grouped_data)

	    	return Response({"business": output_data,"city": sorted(city_data)}, status=status.HTTP_200_OK)
    	else:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)



class BusinessByCategoryStateCity(APIView):
    def get(self, request, state=None,city=None):

    	states = os.getenv("allowed_states").split(",")

    	if state.upper() not in states:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)

    	stateIn = [stateslistsetting[state.upper()],state.upper()]

    	categories = ProfileCategoryLocation.objects.select_related('category_id') \
    	.filter(state__in=stateIn).filter(city=city).values('category_id__name', 'category_id__slug', 'city') \
    	.annotate(category_id__name_count=Count('category_id__name'))

    	#print(categories.query)

    	if categories.exists():

    		grouped_data = defaultdict(list)
    		city_data = []
    		temt_name = []

	    	# Sort categories alphabetically by 'name'
	    	sorted_categories = sorted(list(categories), key=lambda x: x['category_id__name'])

	    	for category in sorted_categories:
	    		first_letter = category['category_id__name'][0].upper()

	    		if category["category_id__name"] not in temt_name:
	    			temt_name.append(category["category_id__name"])
	    			grouped_data[first_letter].append({
		    			"name": category["category_id__name"],
		    			"slug": category["category_id__slug"]
		    		})

	    		if category["city"] not in city_data:
	    			city_data.append(category["city"])

	    	# Convert defaultdict to regular dictionary for JSON serialization
	    	output_data = dict(grouped_data)

	    	return Response({"business": output_data,"city": sorted(city_data)}, status=status.HTTP_200_OK)
    	else:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)



class ServiceByCategory(APIView):
    def get(self, request, service=None):

    	#states = os.getenv("allowed_states").split(",")

    	profile_ids = ProfileCategoryLink.objects.filter(
    		category_id__slug=service
    	).values('profile_id').annotate(
    		num_categories=Count('category_id')
    	).values_list('profile_id', flat=True)

    	if not profile_ids.exists():
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)

    	profiles = Profile.objects.filter(id__in=profile_ids).all().values('title', 'slug').order_by('-updated_at')

    	if profiles.exists():

	    	return Response({"profiles": profiles}, status=status.HTTP_200_OK)
    	else:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)


class ServiceByStateCategory(APIView):
    def get(self, request, service=None, state=None):

    	states = os.getenv("allowed_states").split(",")

    	if state.upper() not in states:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)

    	stateIn = [stateslistsetting[state.upper()],state.upper()]

    	profile_ids = ProfileCategoryLink.objects.filter(
    		category_id__slug=service
    	).values('profile_id').annotate(
    		num_categories=Count('category_id')
    	).values_list('profile_id', flat=True)

    	if not profile_ids.exists():
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)

    	profiles = Profile.objects.filter(id__in=profile_ids).filter(addr_state__in=stateIn).all().values('title', 'slug')

    	if profiles.exists():

	    	return Response({"profiles": profiles}, status=status.HTTP_200_OK)
    	else:
    		return Response({"message": "No data found"}, status=status.HTTP_400_BAD_REQUEST)