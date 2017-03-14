from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os,sys
import django,time
from superlists.wsgi import *


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url="http://"+arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url=cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url==cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        pass
    #    self.browser.quit()
    def check_for_row_in_list_table(self,row_text):
        table=self.browser.find_element_by_id('id_list_table')
        rows=self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.server_url)
        self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        inputbox.send_keys('Buy peacock features')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)

        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text =='1: Buy peacock features' for row in rows),"New to-do item did not appear in table --its text was :\n%s" %(table.text)
        # )

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(10)
        self.check_for_row_in_list_table('1: Buy peacock features')
        self.check_for_row_in_list_table('2: use peacock feathers to make a fly')


      #  self.fail('finish the test')
        self.browser.quit()
        self.browser=webdriver.Firefox()


        self.browser.get(self.server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features',page_text)
        self.assertNotIn('2: use peacock feathers to make a fly',page_text)


        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)


        time.sleep(6)
        francis_list_url=self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEquals(francis_list_url,edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features', page_text)
        self.assertIn('Buy milk', page_text)

    def test_layout_and_styling(self):
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x']+inputbox.size['width'] /2,512, delta=10
        )


