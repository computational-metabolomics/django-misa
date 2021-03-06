# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
#  python manage.py test misa -v 3 --keepdb
#  coverage run --source='.' manage.py test galaxy -v 3 --keepdb
#  coverage report
#  coverage html --omit="admin.py"

import subprocess
import os
import requests

from django.contrib.auth.models import AnonymousUser, User
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from isatools import model as itm
from misa.views import InvestigationListView

def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_response(request)
    return request




class InvestigationListViewTestCase(TestCase):


    def setUp(self):

        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@jacob.com', password='top_secret')

    def test_login_redirect(self):
        """
        Test to check if a guest user is redirect to the login page
        """
        request = self.factory.get('/misa/ilist/')

        request.user = AnonymousUser()
        request = add_middleware_to_request(request, SessionMiddleware)
        response = InvestigationListView.as_view()(request)

        # client acts as a fake website for the request
        response.client = Client()

        self.assertRedirects(response, '/login/?next=/misa/ilist/')

    def test_get(self):
        """
        """
        request = self.factory.get(reverse('ilist'))
        request.user = self.user
        response = InvestigationListView.as_view()(request)
        self.assertEqual(response.status_code, 200) # done without error