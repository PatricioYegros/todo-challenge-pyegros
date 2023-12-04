from django.test import TestCase
from django.urls import reverse

from todo_app.models import Task

class TaskViewTest(TestCase):
    
    def setUp(self):
        Task.objects.create(title="Cocinar", description="Cocinar milanesas")
    
    def test_URL_Exist(self):
        response = self.client.get('/tasks/task/')
        self.assertEqual(response.status_code, 200)
        
    def test_URL_Reverse(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_Correct_Template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'todo_app/index.html')

