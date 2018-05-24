=====
misa
=====

ISA organisation for metabolomic studies with Django

Detailed documentation is in the "docs" directory (todo)

Quick start
-----------

1. Add "gfiles" to your INSTALLED_APPS setting like this (note that this app depends on gfiles and metab::

    INSTALLED_APPS = [
        ...
        'gfiles',
        'metab',
        'misa',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('misa/', include('misa.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add files. Or add as user http://127.0.0.1:8000/upload_gfile/ and
    view files as user http://127.0.0.1:8000/gfile_summary/
