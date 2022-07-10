from utils.Trainee import *
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from datetime import datetime
import os, random, json

# Create your views here.


def root(req):
    print(req.method)
    if req.method == "GET":
        print([x.get_html('#ffffff') for x in read_trainee_database()])
        props = {
            "page": {
                "head": "Leaderboard"
            },
            "html": ''.join([x.get_html('#ffffff') for x in sorted(read_trainee_database(), reverse=True)])
        }
        return render(req, 'leaderboard.html', props)

    elif req.method == "POST":
        post_dict = json.loads(req.body)
        ret = submit_result(post_dict)
        return JsonResponse({'result': ret})
