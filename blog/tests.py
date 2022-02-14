from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Entry
# Create your tests here.

# check Entry Model
class EntryModelTest(TestCase):
    
    # if the entry object name is the same with the entry title
    def test_string_representation(self):
        entry = Entry(title="what ever the title is")
        self.assertEqual(str(entry), entry.title)

    # if the plural name of object in Meta class is right. 
    def test_verbose_name_plural(self):
        # _meta class is currently undocumented.
        # _meta class is created based on the Meta class of the object
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

    # create get absolute url for test
    def test_get_absolute_url(self) :
        user = get_user_model().objects.create(username='user1')
        entry = Entry.objects.create(title='My entry title', author=user)
        self.assertIsNotNone(entry.get_absolute_url())


class ProjectTests(TestCase):
    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class HomePageTests(TestCase) :

    # check if the blog entries show up on the homepage

    def setUp(self) :
        self.user = get_user_model().objects.create(username='user1')

    def test_one_entry(self) :
        Entry.objects.create(title='1-title', body = '1-body', author = self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_two_entry(self) :
        Entry.objects.create(title='1-title', body = '1-body', author = self.user)
        Entry.objects.create(title='2-title', body = '2-body', author = self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')

    # check when there are no entries.
    def test_no_entries(self) :
        response = self.client.get('/')
        self.assertContains(response, 'No blog entries yet.')


class EntryViewTest(TestCase) : 
    def setUp(self) :
        self.user = get_user_model().objects.create(username='user1')
        self.entry = Entry.objects.create(title = '1-title', body = '1-body', author = self.user)

    # From here, require templates blog/entry_detail.html! 
    def test_basic_view(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_title_in_entry(self) :
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.title)

    def test_body_in_entry(self) :
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.body)