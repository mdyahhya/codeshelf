from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.db.models import Count
from .models import Language
from .serializers import LanguageSerializer


# Get all languages or create a new one
class LanguageListView(APIView):
    
    def get(self, request):
        # Fetch all languages from database
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Create a new language entry
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get, update, or delete a specific language
class LanguageDetailView(APIView):
    
    def get_language(self, pk):
        # Helper method to get language by ID
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            return None
    
    def get(self, request, pk):
        # Get single language details
        language = self.get_language(pk)
        if language is None:
            return Response({'error': 'Language not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)
    
    def put(self, request, pk):
        # Update a language
        language = self.get_language(pk)
        if language is None:
            return Response({'error': 'Language not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        # Delete a language
        language = self.get_language(pk)
        if language is None:
            return Response({'error': 'Language not found'}, status=status.HTTP_404_NOT_FOUND)
        language.delete()
        return Response({'message': 'Language deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# Dashboard view - shows summary and list of languages
def dashboard_view(request):
    # Get all languages
    languages = Language.objects.all()
    
    # Calculate stats by category
    total = languages.count()
    fsd = languages.filter(category='FSD').count()
    cs = languages.filter(category='CS').count()
    ds = languages.filter(category='DS').count()
    
    # Pass data to template
    context = {
        'languages': languages,
        'total_languages': total,
        'fsd_count': fsd,
        'cs_count': cs,
        'ds_count': ds,
    }
    
    return render(request, 'tracker/dashboard.html', context)

import requests
from django.http import JsonResponse

# Import sample languages from external API
def import_languages_view(request):
    # Use GitHub's language colors API as external data source
    api_url = "https://raw.githubusercontent.com/ozh/github-colors/master/colors.json"
    
    try:
        # Fetch data from external API
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        languages_data = response.json()
        
        # Sample languages to import (picking a few relevant ones)
        sample_langs = {
            'Python': {'category': 'FSD', 'proficiency': 'Advanced', 'desc': 'Backend, Data Science, ML'},
            'JavaScript': {'category': 'FSD', 'proficiency': 'Advanced', 'desc': 'Frontend and backend web development'},
            'Java': {'category': 'FSD', 'proficiency': 'Intermediate', 'desc': 'Enterprise applications'},
            'C++': {'category': 'CS', 'proficiency': 'Intermediate', 'desc': 'System programming, security'},
            'R': {'category': 'DS', 'proficiency': 'Beginner', 'desc': 'Statistical analysis and data visualization'},
            'SQL': {'category': 'DS', 'proficiency': 'Intermediate', 'desc': 'Database queries and management'},
        }
        
        imported_count = 0
        skipped_count = 0
        
        # Import languages that don't already exist
        for lang_name, info in sample_langs.items():
            # Check if language exists in external API data
            if lang_name in languages_data:
                # Check if we already have this language
                if not Language.objects.filter(name=lang_name).exists():
                    Language.objects.create(
                        name=lang_name,
                        category=info['category'],
                        proficiency=info['proficiency'],
                        description=info['desc'],
                        resources=f"Imported from external API - GitHub language data"
                    )
                    imported_count += 1
                else:
                    skipped_count += 1
        
        return JsonResponse({
            'status': 'success',
            'message': f'Imported {imported_count} languages, skipped {skipped_count} existing',
            'imported': imported_count,
            'skipped': skipped_count
        })
        
    except requests.RequestException as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to fetch from external API: {str(e)}'
        }, status=500)

