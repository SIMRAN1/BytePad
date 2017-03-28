BytePad
=======
Web service to download previous years' question papers &amp; solutions.


Installation Instructions
-------------------------
1. Install dependencies - `pip install -r requirements.txt`
2. Make a new Postgres DB named `bytepad`
3. Run database migrations - `python manage.py migrate`
4. Install django-watson - `python manage.py installwatson`
5. Update watson index - `python manage.py buildwatson`
