from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import redis
def hello(request):
	strs=redis.__file__
	strs+="<br>"
	r = redis.Redis(host='db',port=6379,db=0)
	info =r.info()
	strs+=("Set Hi <br>")
	r.set('Hi','HelloWorld-APP2')
	strs+=("Get Hi: %s <br>" % r.get('Hi'))
	strs+=("Redis Info: <br>")
	strs+=("key :Info Value")
	for key in info:
		strs+=("%s:%s <br>" % (key,info[key]))
	return HttpResponse(strs)
