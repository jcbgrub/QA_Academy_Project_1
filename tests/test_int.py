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

# Set test variables for test admin user
test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"

# set variables for book entry
test_first_name = 'test'
test_surname = 'test'
test_title ='test'
test_pages ='123'
test_language = 'test'

# variables rate form
test_admin_rate ='2'
test_admin_comment = 'test'

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

	def tearDown(self):
		self.driver.quit()
		print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

	def test_server_is_up_and_running(self):
		response = urlopen("http://localhost:5000")
		self.assertEqual(response.code, 200)

class TestRegistration(TestBase):

	def test_registration(self):
		"""
		Test that a user can create an account using the registration form
		if all fields are filled out correctly, and that they will be 
		redirected to the login page
		"""

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

	def test_login(self):
		# Click login menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)
		# Fill in login form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/input').click()
		time.sleep(1)

		# Assert that browser redirects to main page
		assert url_for('main_lib') in self.driver.current_url

# class Test_Adding_entries(TestBase):
	def test_new_entry(self):

		# Click rate menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
		time.sleep(1)
		# Fill in lorategin form
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_first_name)
		self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_surname)
		self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_title)
		self.driver.find_element_by_xpath('//*[@id="pages"]').send_keys(test_pages)
		self.driver.find_element_by_xpath('//*[@id="language"]').send_keys(test_language)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# Assert that browser redirects to main page
		assert url_for('main_lib') in self.driver.current_url

	def test_rate(self):

		# Click rate menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[3]').click()
		time.sleep(1)
		# Fill in rate form
		self.driver.find_element_by_xpath('//*[@id="rating"]').send_keys(test_admin_rate)
		self.driver.find_element_by_xpath('//*[@id="comment"]').send_keys(test_admin_comment)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		# Assert that browser redirects to main library page
		assert url_for('main_lib') in self.driver.current_url

class Test_changing_entries(TestBase):
	def test_update_lib(self):
		# from main lib page click the link to the update page
		self.driver.find_element_by_xpath('/html/body/div[2]/p/a[1]').click()
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

	# the add movie page
	def test_delete_books(self):
		# Click rate menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
		time.sleep(1)
		# Fill in lorategin form
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_first_name)
		self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_surname)
		self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_title)
		self.driver.find_element_by_xpath('//*[@id="pages"]').send_keys(test_pages)
		self.driver.find_element_by_xpath('//*[@id="language"]').send_keys(test_language)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
	# from home page click the link to the update page
		self.driver.find_element_by_xpath('/html/body/div[2]/p/a[2]').click()
		assert url_for('main_lib') in self.driver.current_url


if __name__ == "__main__":
	unittest.main(port=5000)

