import test3
from django.shortcuts import render_to_response,redirect
from django.utils import timezone
from .models import Appreq
from .forms import PostForm
from .forms import RegForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import subprocess
from calendar import monthrange
from datetime import datetime
@csrf_exempt
def appreq(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
            appreq = form.save()
            appreq.save()
            test3.get_credentials()
            test3.main()
    form = PostForm()
    return render_to_response( 'app/appreq.html', {'form':form}, RequestContext(request))
@csrf_exempt
def users(request):
    if request.method == 'POST':
      form = RegForm(request.POST)
      if form.is_valid():
          reg = form.save()
          reg.save()
    form = RegForm()
    return render_to_response( 'app/register.html', {'regform':form}, RequestContext(request))

def named_month(month_number):

	"""
	Return the name of the month, given the number.
	"""
	return datetime(1900, month_number, 1).strftime("%B")

def this_month(request):
	"""
	Show calendar of readings this month.
	"""
	today = datetime.now()
	return calendar(request, today.year, today.month)

def calendar(request, year, month, series_id=None):
	"""
	Show calendar of readings for a given month of a given year.
	``series_id``
	The reading series to show. None shows all reading series.
	"""
	my_year = int(year)
	my_month = int(month)
	my_calendar_from_month = datetime(my_year, my_month, 1)
	my_calendar_to_month = datetime(my_year, my_month, monthrange(my_year, my_month)[1])

	my_reading_events = Appreq.objects.filter(start_date=my_calendar_from_month).filter(end_date=my_calendar_to_month)
	if series_id:
		my_reading_events = my_reading_events.filter(series=series_id)

	# Calculate values for the calendar controls. 1-indexed (Jan = 1)
	my_previous_year = my_year
	my_previous_month = my_month - 1
	if my_previous_month == 0:
		my_previous_year = my_year - 1
		my_previous_month = 12
	my_next_year = my_year
	my_next_month = my_month + 1
	if my_next_month == 13:
		my_next_year = my_year + 1
		my_next_month = 1
	my_year_after_this = my_year + 1
	my_year_before_this = my_year - 1
	return render_to_response("cal_template.html", { 'readings_list': my_reading_events,
														'month': my_month,
														'month_name': named_month(my_month),
														'year': my_year,
														'previous_month': my_previous_month,
														'previous_month_name': named_month(my_previous_month),
														'previous_year': my_previous_year,
														'next_month': my_next_month,
														'next_month_name': named_month(my_next_month),
														'next_year': my_next_year,
														'year_before_this': my_year_before_this,
														'year_after_this': my_year_after_this,
	}, RequestContext(request))
