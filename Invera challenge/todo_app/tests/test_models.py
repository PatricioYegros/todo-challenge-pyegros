from django.test import TestCase

from todo_app.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(title="Cocinar", description="Cocinar milanesas")
        Task.objects.create(title="Ordenar", description="La pieza")
        
    def test_tasks(self):
        cocinar = Task.objects.get(title="Cocinar")
        ordenar = Task.objects.get(title="Ordenar")
        self.assertEqual(cocinar.description,"Cocinar milanesas")
        self.assertEqual(ordenar.description,"La pieza")