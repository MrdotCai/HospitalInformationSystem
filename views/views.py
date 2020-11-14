from Sheets import db_intfs
from django.views import View
from django.http import HttpResponse
from django.middleware.csrf import get_token
import json
from django.shortcuts import render

# Create your views here.

def getToken(request):
    token = get_token(request)
    return HttpResponse(
        json.dumps({"token": token}), content_type="application/json,charset=utf-8"
    )


class Index(View):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        # db_intfs.init_database()
        return render(request=request, template_name="index.html")