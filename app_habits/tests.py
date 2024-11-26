from django.urls import reverse
from rest_framework.test import APITestCase
from app_habits.models import Habit
from rest_framework import status

from app_habits.serializers import HabitSerializer
# from app_habits.validators import HabitValidate, HabitModelValidate
from app_user.models import User


class HabitModelTestCase(APITestCase):
    """Тест модели привычки"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(email='testuser@test.test', password='test')
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания привычки"""
        habit = Habit.objects.create(
            user=self.user,
            place='В деревне',
            time='Когда поют петухи',
            action='Спеть вместе с ними',
            reward='Похвала мамы',
            lead_time=120,
        )
        self.assertEqual(habit.user, self.user)
        self.assertEqual(habit.place, 'В деревне')
        self.assertEqual(habit.time, 'Когда поют петухи')
        self.assertEqual(habit.action, 'Спеть вместе с ними')
        self.assertFalse(habit.is_pleasant)
        self.assertEqual(habit.linked_habit, None)
        self.assertEqual(habit.periodicity, 1)
        self.assertEqual(habit.reward, 'Похвала мамы')
        self.assertEqual(habit.lead_time, 120)
        self.assertFalse(habit.is_public)


class HabitViewTestCase(APITestCase):
    """Тесты контроллеров привычки"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(email='testuser@test.test', password='test')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place='В деревне',
            time='Когда поют петухи',
            action='Спеть вместе с ними',
            reward='Похвала мамы',
            lead_time=120,
        )

    def test_habit_retrieve(self):
        """Тестирование вывода одной привычки"""
        url = reverse('app_habits:habit-get', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('action'), self.habit.action)

    def test_course_update(self):
        """Тестирование изменения одной привычки"""
        url = reverse('app_habits:habit-update', args=(self.habit.pk,))
        data = {'lead_time': 100}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lead_time'), 100)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        url = reverse('app_habits:habit-create')
        data = {
            'place': 'На диване',
            'time': 'после чаечка',
            'action': 'учить питон конечо',
            'habit_link': self.habit.pk,
            'lead_time': 120,
            'is_publiс': True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habits_list(self):
        """Тестирование вывода всех привычек"""
        url = reverse('app_habits:habit-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.habit.pk,
                    'user': self.user.id,
                    'condition': "Я буду Спеть вместе с ними Когда поют петухи В деревне",
                    'periodicity': self.habit.periodicity,
                    "reward_or_linked_habit": "reward 'Похвала мамы'",
                    'lead_time': self.habit.lead_time,
                    'is_pleasant': self.habit.is_pleasant,
                    'is_public': self.habit.is_public,
                }
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_delete(self):
        """Тестирование удаления одной привычки"""
        url = reverse('app_habits:habit-delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)


class HabitSerializerTestCase(APITestCase):
    """Тестирование сериализатора"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(email='testuser@test.test', password='test')
        self.habit = Habit.objects.create(
            user=self.user,
            place='Спиртзавод',
            time='Сосранья',
            action='Тусить',
            is_pleasant=True,
            lead_time=120,
        )

    def test_valid_data(self):
        """Проверка правильных значений"""
        data = {
            "user": self.user.id,
            'place': 'Спиртзавод',
            'time': "Сосранья",
            'action': 'Тусить',
            'is_pleasant': False,
            'linked_habit': self.habit.pk,
            'periodicity': 3,
            'reward': None,
            'lead_time': 120,
            'is_public': True,
        }
        serializer = HabitSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """Проверка правильных значений"""
        data = {
            'linked_habit': 'some_value',  # должно быть habit.pk
            'periodicity': 'some_value',  # должно быть число
            'lead_time': 'some_value',  # должно быть число
            'is_public': 123,  # должно быть bool
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('linked_habit', serializer.errors)
        self.assertIn('periodicity', serializer.errors)
        self.assertIn('lead_time', serializer.errors)
        self.assertIn('is_public', serializer.errors)