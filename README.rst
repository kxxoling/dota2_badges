============
Dota2 badges
============

This is a project built on Django and Opendota API, and uses Redis as data cache.

Install
=======

It's strongly suggested to use ``pipenv`` to install and manage the Python dependencies!

    pipenv install && pipenv shell

And also, you need to have Redis installed and started, assuming it's running at ``redis://localhost:6379``

Running
=======

Now you can run ``./manage.py runserver`` and open link like ``http://localhost:8000/121230511/mmr.svg`` to get your MMR badge:

.. image:: https://cdn.rawgit.com/kxxoling/dota2_badges/master/mmr.svg

