from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import CommentForm
