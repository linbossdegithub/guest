from django.http import JsonResponse
from test_test.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist
import json
import logging
def add_event(request):
    eid = request.POST.get("eid","")
    name = request.POST.get("name","")
    limit = request.POST.get("limit","")
    status = request.POST.get("status","")
    address = request.POST.get("address","")
    start_time = request.POST.get("start_time","")
    received_json_data = request.body
    logging.error(type(received_json_data))
    if eid =='' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status':10021,'message':'parameter error '})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})
    result = Event.objects.filter(name=name)
    if result:
        JsonResponse({'status':10023,'message':'event name already exists'})
    if status == '':
        status = 1
    try:
        Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024,'message':error})
    return JsonResponse({'status':200,'message':'add event success'})
def get_event_list(request):
	eid =request.GET.get("eid","")
	name =request.GET.get("name","")
	if eid == '' and name == '':
		return JsonResponse({'status':10021,'message':'parameter error'})
	if eid !='':
		event = {}
		try:
			result = Event.objects.get(id=eid)
		except ObjectDoesNotExist:
			return JsonResponse({'status':10022,'message':'query result is empty'})
		else:
			event['name'] = result.name
			event['limit'] = result.limit
			event['status'] = result.status
			event['address'] = result.address
			event['start_time'] = result.start_time
			return JsonResponse({'status':200,'message':'success','data':event})
	if name != '':
		datas=[]
		results =Event.objects.filter(name__contains=name)
		if results:
			for r in results:
				event = {}
				event['name'] =r.name
				event['limit'] = r.limit
				event['status'] = r.status
				event['address'] = r.address
				event['start_time'] = r.start_time
				datas.append(event)
			return JsonResponse({'status':200,'message':'success','data':datas})
		else:
			return JsonResponse({'status':10022,'message':'query result is empty'})



