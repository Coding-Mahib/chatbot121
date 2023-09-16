from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chatter import get_resp

# Create your views here.
def home(req):
	return render(req, 'index.html')
@csrf_exempt
def api(req):
	if req.method == 'POST':
		text = req.POST['text']
		return HttpResponse(get_resp(text))
		
