from django.test import TestCase
from sign.models import Event, Guest
from django.contrib.auth.models import User
# Create your tests here.


class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='Shenzhen', start_time='2019-01-03 17:00:00')
        Guest.objects.create(id=1, event_id=1, realname='alen', phone='13713713722', email='alen@mail.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, 'Shenzhen')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13713713722')
        self.assertEqual(result.realname, 'alen')
        self.assertFalse(result.sign)


class IndexPageText(TestCase):
    '''测试index登录页面'''

    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    '''测试登录动作'''
    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin')

    def test_add_admin(self):
        '''测试添加用户'''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@mail.com')
        #self.assertEqual(user.password, 'admin2')

    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        test_data = {'username': '', 'password': ''}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("username or password error!", response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("username or password error!", response.content)

    def test_login_action_username_password_success(self):
        ''' 用户名密码正确 '''
        test_data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)
        #self.assertIn("username or password error!", response.content)


class EventManageTest(TestCase):


    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin')
        Event.objects.create(name='xiaomi', limit=2000, address='shenzhen', status=1, start_time='2019-01-03 12:30:00')
        self.login_user = {'username': 'admin', 'password': 'admin'}

    def test_event_manage_success(self):
        '''测试发布会:小米发布会'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("xiaomi", response.content)
        self.assertIn("shenzhen", response.content)

    def test_event_manage_serach_success(self):
        '''测试发布会搜索'''
        response = self.client.post('/login_action', data=self.login_user)
        response = self.client.post('/search_name/', {"name": "xiaomi"})
        self.assertEqual(response.status_code, 302)
        self.assertIn(b"xiaomi", response.content)
        self.assertIn(b"shenzhen", response.content)
