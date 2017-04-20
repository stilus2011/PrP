from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	template = """
	<doctype html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>Homepage</title>
	</head>
	<body>
	<h1>Homepage</h1>
	</body>
	</html>
	"""
	return HttpResponse("HOMEPAGE")