import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db, bcrypt
from application.models import Users, book_library,main_library
from os import getenv

class TestBase(TestCase):
	def create_app(self):
		# pass in configurations for test database
		config_name = 'testing'
		app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
				SECRET_KEY=getenv('TEST_SECRET_KEY'),
				WTF_CSRF_ENABLED=False,
				DEBUG=True
				)
		return app

	def setUp(self):
		"""
		Will be called before every test
		"""
		# ensure there is no data in the test database when the test starts
		db.session.commit()
		db.drop_all()
		db.create_all()

		# create test admin user
		hashed_pw = bcrypt.generate_password_hash('admin2016')
		admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)

		# create test non-admin user
		hashed_pw_2 = bcrypt.generate_password_hash('test2016')
		employee = Users(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)

		# save users to database
		db.session.add(admin)
		db.session.add(employee)
		db.session.commit()

	def tearDown(self):
		"""
		Will be called after every test
		"""

		db.session.remove()
		db.drop_all()

class TestViews(TestBase):
	# Test that login accessible without login
	def test_login_view(self):
		response = self.client.get(url_for('login'))
		self.assertEqual(response.status_code, 200)
	# Test that register is accessible without login
	def test_register_view(self):	
		response = self.client.get(url_for('register'))
		self.assertEqual(response.status_code, 200)
	
	# Tests that if user not logged in is redirected to the loging page
	def test_notloggedin_main_lib(self):
		response1 = self.client.get(url_for("main_lib"), follow_redirects = True)
		self.assertEqual(response1.status_code, 200)
		self.assertIn(b"login", response1.data)
	# Tests that if user not logged in is redirected to the loging page
	def test_notloggedin_new_entry(self):
		response2 = self.client.get(url_for("new_entry"), follow_redirects = True)
		self.assertEqual(response2.status_code, 200)
		self.assertIn(b"login", response2.data)
	# Tests that if user not logged in is redirected to the loging page
	def test_notloggedin_rate(self):
		response3 = self.client.get(url_for("rate"), follow_redirects = True)
		self.assertEqual(response3.status_code, 200)
		self.assertIn(b"login", response3.data)
			# Tests that if user not logged in is redirected to the loging page
	def test_notloggedin_update_lib(self):
		response4 = self.client.get(url_for("update_lib",book_id = 1), follow_redirects = True)
		self.assertEqual(response4.status_code, 200)
		self.assertIn(b"login", response4.data)

class Testadding(TestBase):
	def test_new_entry(self):
	# Test that when I add a new book, I am redirected to the homepage with the new post visible
		with self.client:
			self.client.post(url_for('login'), data=dict(email='admin@admin.com',password='admin2016'),follow_redirects=True)
			response = self.client.post(
				'/new_entry',
				data=dict(
					first_name = "Test name",
					surname = "Test suname",
					title = "Test Title",
					pages = "123",
					language = "Test language"
				),
				follow_redirects=True
			)
			self.assertIn(b'Test Title', response.data)
			self.assertEqual(response.status_code, 200)

	def test_rate(self):
	# Test that when I add a new book, I am redirected to the homepage with the new post visible - ADMIN
		with self.client:
			self.client.post(url_for('login'), data=dict(email='admin@admin.com',password='admin2016'),follow_redirects=True)
			response = self.client.post(
				'/rate',
				data=dict(
				rating = '1',
				comment = 'Test comment'

				),
				follow_redirects=False
				# potray all  is missing.
			)
			self.assertIn(b'Test comment', response.data)
			self.assertEqual(response.status_code, 200)

class Testupdating(TestBase):
	# Test that when I update a new book, I am redirected to the homepage with the new post visible
	def test_update_lib(self):
		with self.client:
			self.client.post(url_for("login"),data = dict(username = "test", password = "password"),follow_redirects = True)
			
			response = self.client.post(
				url_for("main_lib", book_id = 1),
				data = dict(
					first_name = "Test update name",
					surname = "Test updatesuname",
					title = "Test update Title",
					pages = "123",
					language = "Test update language"
				),
				follow_redirects=True
			)
			self.assertIn(b"Test update Title", response.data),
			self.assertEqual(response.status_code, 200)


class TestUserCreation(TestBase):
	# test to register new user
	def test_register(self):
		with self.client:
			response = self.client.post(
				url_for('register'),
				data = dict(
					first_name = 'john',
					last_name = 'doe',
					email = 'john@doe.com',
					password = 'test123test',
					confrim_password = 'test123test',
				),
				follow_redirects = True
			)
			self.assertIn(b"Login", response.data)
			self.assertEqual(response.status_code, 200)
# test to logout
	def test_logout(self):
		with self.client:
			response = self.client.get(
				'/logout',
				follow_redirects = True
			)
			self.assertIn(b'Sign In', response.data)
			self.assertEqual(response.status_code, 200)
# test to log in
	def test_login(self):
		with self.client:
			response = self.client.post(
				url_for('login'),
				data = dict(
					first_name = 'john'.
					last_name = 'doe',
					email = 'john@doe.com',
					password = 'test123test',
					confrim_password = 'test123test',
				),
				follow_redirects = True
			)
			self.assertIn(b"main_lib", response.data)
			self.assertEqual(response.status_code, 200)
			