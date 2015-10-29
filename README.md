reallylonglink
==========

Make links into really long links.

Setup
----------

Create a postgres user named reallylonglink and a database owned by this user
and named the same.

    $ mkvirtualenv reallylonglink --python=`which python3`
    $ pip install -r requirements.txt
    $ envdir /path/to/your/envdir ./manage.py migrate

Development
----------

Commands must be preceded with the envdir location, like so:

    $ envdir /path/to/your/envdir ./manage.py some_radical_command --option sure
