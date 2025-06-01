from django.http import HttpResponse
from currentApp.models import Person
import datetime

def current_time(request):
    now = datetime.datetime.now()
    print(now)
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def name_db(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    if first_name and last_name:
        person = Person.objects.create(first_name = first_name, last_name = last_name)
        return HttpResponse(f"Added {person.first_name} {person.last_name} to DB. ")

    html = "<html><body>No first & last name</body></html>"
    return HttpResponse(html)
