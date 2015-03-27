# Django Extrasettings

Django Extrasettings lets you extend the settings system of Django with database-stored settings that can be edited live. It uses [JSON Schema](http://json-schema.org/) to define the settings schema and [json-editor](http://jeremydorn.com/json-editor/) in the admin interface to edit the settings. Works with Django 1.7

### Installation

Install Django plugins with pip:

```sh
pip install django-extrasettings
```

Add 'extrasettings' to the list of installed apps in your `settings.py` file:

```python
...
'extrasettings',
...
```

Add a `EXTRASETTINGS_DIR` setting to your `settings.py` with the directory where you are going to store your plugins. For instance:

```python
...
EXTRASETTINGS_DIR = os.path.join(BASE_DIR, 'esettings')
...
```

Execute `./manage.py migrate`

### Configuring settings

Imagine that you want to configure a list of special users with attributes and want to be able to edit it live. This is something you'd typically to as a Django Model, but it's just an example. First define the schema and save it into a .json file located in your EXTRASETTINGS_DIR. The name of the file will be the name of the settings object. Call it `users.json`

```json
{
  "title": "Special Users",
  "type": "array",
  "format": "table",
  "items": {
    "title": "User",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "User name"
        },
        "sex": {
            "title": "Gender",
            "type": "string",
            "enum": [
                "male",
                "female"
            ]
        },
        "age": {
            "title": "Age",
            "type": "integer",
            "minimum": 1,
            "maximum": 99
        }
    }
  }
}
```

If you visit the admin site, You'll now notice a list of Django Extrasettings. It has only one item, called "users" just like the file we just wrote minus ".json".

Editing it shows an interface appropriate for editing the schema we defined:

![Screenshot 1](http://i.imgur.com/sGDEiOc.png)

Within your project you can now access the settings in this way:

```python
from django.http import HttpResponse

import extrasettings

def home(request):
    html = '<html><body><h1>Special Users</h1><ul>'
    for user in extrasettings.users:
        html += '<li>%s is a %s of %d</li>' % (user['name'], user['sex'], user['age'])
    html += '</ul></body></html>'
    return HttpResponse(html)
```

This will print "Batman is a male of 78" and "Shirley Temple is a female of 5".



