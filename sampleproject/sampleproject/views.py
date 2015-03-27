from django.http import HttpResponse

import extrasettings

def home(request):
    html = '<html><body><h1>Special Users</h1><ul>'
    for user in extrasettings.users:
        html += '<li>%s is a %s of %d</li>' % (user['name'], user['sex'], user['age'])
    html += '</ul></body></html>'
    return HttpResponse(html)