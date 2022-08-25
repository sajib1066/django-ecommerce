# Django E-commerce Website.

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/sajib1066/django-ecommerce.git

```

--> Move into the directory where we have the project files : 
```bash
cd django-ecommerce

```

--> Create a virtual environment :
```bash
# Create our virtual environment
python -m venv venv

```

--> Activate the virtual environment : <br><br>
windows
```bash
venv\scripts\activate

```
linux
```bash
source venv/bin/activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Migrate Database
```bash
python manage.py migrate

```

--> Create Super User
```bash
python manage.py createsuperuser

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Landing page
</p>
<img src="https://user-images.githubusercontent.com/47305153/186664016-c0aece16-cfe3-475f-8ca6-c5cac62c9f88.PNG">
</td> 
<td width="50%">
<br>
<p align="center">
  More view on landing page
</p>
<img src="https://user-images.githubusercontent.com/47305153/186664028-a661886b-88b5-474d-bcd8-1162258ab6d1.PNG">  
</td>
</table>


## Documentation
You can check up django documentation page for any further information.
[Django Docs](https://docs.djangoproject.com/en/4.0/)
