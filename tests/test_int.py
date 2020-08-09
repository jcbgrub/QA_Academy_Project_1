import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Users, book_library, main_library
from werkzeug.security import generate_password_hash, check_password_hash

# Set test variables for test admin user
test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"

class TestBase(LiveServerTestCase):

	def create_app(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DB_URI'))
		app.config['SECRET_KEY'] = getenv('TEST_SECRET_KEY')
		return app

	def setUp(self):
		"""Setup the test driver and create test users"""
		print("--------------------------NEXT-TEST----------------------------------------------")
		chrome_options = Options()
		chrome_options.binary_location = "/usr/bin/chromium-browser"
		chrome_options.add_argument("--headless")
		self.driver = webdriver.Chrome(executable_path="/home/jacob_hp_grub/increment/chromedriver", chrome_options=chrome_options)
		self.driver.get("http://localhost:5000")
		db.session.commit()
		db.drop_all()
		db.create_all()

		# creating a test user

		testuser = Users(
   			id = 1,
			first_name = 'testy',
			last_name = 'Mctestface',
			email = 'test@test.com',
			password = 'test123'
		)
		# creating a test book
		Test_book = book_library(
			id = 1,
			first_name = 'test',
			surname = 'test',
			title ='test',
			pages =123,
			language = 'test',
			user_id = 1
		)
		# creating a test rating
		Test_rate = main_library(
			id = 1,
			rating = 2,
			comment = 'test',
			user_id = 1,
			book_id = 1
		)
		# adds the test data to the database
		db.session.add(testuser)
		db.session.add(Test_book)
		db.session.add(Test_rate)
		db.session.commit()


	def tearDown(self):
		self.driver.quit()
		print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

	def test_server_is_up_and_running(self):
		response = urlopen("http://localhost:5000")
		self.assertEqual(response.code, 200)

class TestRegistration(TestBase):

	def test_registration(self):
		# Click register menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
		time.sleep(1)

		# Fill in registration form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)

		# Assert that browser redirects to login page
		assert url_for('login') in self.driver.current_url

class Testlogin(TestBase):
	def test_login(self):
		# Click login menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)
		assert url_for('login') in self.driver.current_url
		# Fill in login form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('test@test.com')
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('test123')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# Assert that browser redirects to main page
		assert url_for('main_lib') in self.driver.current_url

class Test_new_entry(TestBase):
	def test_new_entry(self):
		# Click login menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)
		assert url_for("login") in self.driver.current_url
		# Fill in login form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('test@test.com')
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('test123')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)

		# Click rate menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
		assert url_for("new_entry") in self.driver.current_url
		time.sleep(1)
		# Fill in lorategin form
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys('test name')
		self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys('test surname')
		self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('test title')
		self.driver.find_element_by_xpath('//*[@id="pages"]').send_keys(123)
		self.driver.find_element_by_xpath('//*[@id="language"]').send_keys('test lang')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# Assert that browser redirects to main page
		assert url_for('main_lib') in self.driver.current_url

class Test_rate(TestBase):
	def test_rate(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)
		assert url_for("login") in self.driver.current_url
		# Fill in login form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('test@test.com')
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('test123')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# Assert that browser redirects to main page
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		assert url_for('main_lib') in self.driver.current_url

		# Click rate menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[3]').click()
		assert url_for('rate') in self.driver.current_url
		time.sleep(1)
		# Fill in rate form
		self.driver.find_element_by_xpath('//*[@id="rating"]').send_keys(2)
		self.driver.find_element_by_xpath('//*[@id="comment"]').send_keys('test')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# Assert that browser redirects to main library page
		assert url_for('main_lib') in self.driver.current_url

class Test_changing_entries(TestBase):
	def test_update_lib(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)
		assert url_for("login") in self.driver.current_url
		# Fill in login form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('test@test.com')
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('test123')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# from main lib page click the link to the update page
		self.driver.find_element_by_xpath('/html/body/div[2]/p/a[1]').click()
		assert url_for('update_lib/',book_id =1) in self.driver.current_url
		# fill the form
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_first_name)
		self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_surname)
		self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_title)
		self.driver.find_element_by_xpath('//*[@id="pages"]').send_keys(test_pages)
		self.driver.find_element_by_xpath('//*[@id="language"]').send_keys(test_language)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# Assert that browser redirects to main library page
		assert url_for('main_lib') in self.driver.current_url

	# the deleting a book
	def test_delete_books(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)
		assert url_for("login") in self.driver.current_url
		# Fill in login form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('test@test.com')
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('test123')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		assert url_for('main_lib') in self.driver.current_url
		self.driver.find_element_by_xpath('//*[@id="submit"]').click(/html/body/div[2]/p/a[2])

if __name__ == "__main__":
	unittest.main(port=5000)

