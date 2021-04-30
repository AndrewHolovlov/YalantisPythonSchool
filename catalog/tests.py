import datetime
from django.test import TestCase

from .models import Course
from .serializers import CourseSerializer


class CourseViewTest(TestCase):
    def setUp(self):
        self.course1 = Course.objects.create(name='Course 1', start_date='2021-04-29', end_date='2021-05-29', number_of_lectures=20)
        self.course2 = Course.objects.create(name='Course 2', start_date='2021-04-29', end_date='2021-05-29', number_of_lectures=20)
        self.course3 = Course.objects.create(name='Course 3', start_date='2021-04-29', end_date='2021-05-29', number_of_lectures=20)
        self.valid = {
            "name": "Course 4",
            "start_date": "2021-04-28",
            "end_date": "2021-05-28",
            "number_of_lectures": 20
        }
        self.invalid = {
            "name": "",
            "start_date": "2021-04-28",
            "end_date": "2021-05-28",
            "number_of_lectures": 20
        }

    def tearDown(self):
        self.course1.delete()
        self.course2.delete()
        self.course3.delete()

    def test_all_course(self):
        response = self.client.get('/api/courses/')
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_create_vilid_course(self):
        response = self.client.post('/api/courses/', data=self.valid, content_type='application/json')
        course = Course.objects.get(name="Course 4")
        serializer = CourseSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 201)

    def test_create_invilid_course(self):
        response = self.client.post('/api/courses/', data=self.invalid, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_valide_single_course(self):
        response = self.client.get('/api/courses/1')
        serializer = CourseSerializer(self.course1)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_invalide_single_course(self):
        response = self.client.get('/api/courses/20')
        self.assertEqual(response.status_code, 404)

    def test_update_valid_course(self):
        response = self.client.put('/api/courses/1', data=self.valid, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_invalid_course(self):
        response = self.client.put('/api/courses/1', data=self.invalid, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_valid_course(self):
        response = self.client.delete('/api/courses/1')
        self.assertEqual(response.status_code, 204)

    def test_delete_invalid_course(self):
        response = self.client.delete('/api/courses/20')
        self.assertEqual(response.status_code, 404)


class CourseTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Course Test', start_date='2021-04-29', end_date='2021-05-29', number_of_lectures=20)
        self.course.save()

    def tearDown(self):
        self.course.delete()

    def test_read_course(self):
        course = Course.objects.get(name='Course Test')
        self.assertEqual(course.name, 'Course Test')
        self.assertEqual(course.start_date, datetime.date(2021, 4, 29))
        self.assertEqual(course.end_date, datetime.date(2021, 5, 29))
        self.assertEqual(course.number_of_lectures, 20)

    def test_update_course(self):
        self.course.name = 'Course new Test'
        self.course.save()
        course = Course.objects.get(name='Course new Test')
        self.assertEqual(course.name, 'Course new Test')
