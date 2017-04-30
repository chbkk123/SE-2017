=====
Blog
=====

 Note app based by blog app by django


Quick start
-----------

1. Add "blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'blog',
    ]

2. Include the note-app URLconf in your project urls.py like this::

    url(r'^blog/', include('blog.urls')),

3. Run `python manage.py migrate` to create the blog models.

4. Start the development server and visit  http://127.0.0.1:8000/admin/ to create superuser for using note app.
   

5. Visit http://127.0.0.1:8000/ to start note app.