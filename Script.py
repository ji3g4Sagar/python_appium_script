from time import sleep
import logging
from Motion import swipePage, enterContext, clickAndTap
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,\
	expected_conditions


class script():
	logging.basicConfig(filename=__name__+'.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level = logging.ERROR)
	def __init__(self, driver):
		self.driver = driver
		self.SP = swipePage(self.driver)
		self.EC = enterContext(self.driver)
		self.CT = clickAndTap(self.driver)
		self.logger = logging.getLogger('sagar_log')
		self.logger.setLevel(logging.DEBUG)
		self.handler = logging.FileHandler('Script.log', 'a')
		self.handler.setLevel(logging.DEBUG)
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
		self.handler.setFormatter(self.formatter)
		self.logger.addHandler(self.handler)

	def basicMotion(self):
		self.SP.swipLeft(n=4)
		sleep(1)
		
	def find_Toast(self,message,timeout=5,poll_frequency = 0.5):  #xpath查找toast值
		
		#logging.info("獲取toast值---'%s'" %message)
		try:
			message = '//*[@text=\'{}\']'.format(message)
			#toast_loc = ("xpath",".//*[contains(@text,'%s')]" %message)
			#WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(toast_loc))
			WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(message))
			
			#logging.info("查找到toast--'%s'"%message)
			self.logger.info("Find toast!!\n")
			return True
		except:
			#logging.info("未查找到toast--'%s'"%message)
			self.logger.info("Not find toast")
			return False
	def find_Toast2(self,message):  #查找toast值
		
		#self.logger.info(" find toast value---'%s'" %(message))
		try:
			#message = '//*[@text=\'{}\']'.format(message)
			WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
			self.logger.info("find toast!!")
			#self.logger.info("查找到toast----%s"%message)
			return True
		except:
			self.logger.info("Not find toast!!")
			#self.logger.info("未查找到toast----%s"%message)
			return False
	
	def testOne(self): #正常登陸
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		sleep(1)
		self.EC.enter("#","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("#", "com.lavidatec.wacare:id/et_login_pass")
		sleep(1)
		self.CT.click("com.lavidatec.wacare:id/tv_login")        
		sleep(2)
	def testTwo(self):#更改國籍
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		sleep(1)
		self.EC.enter("#","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("#", "com.lavidatec.wacare:id/et_login_pass")
		sleep(1)
		self.CT.click("com.lavidatec.wacare:id/linear_flag_border")
		sleep(1)
		self.CT.click("com.lavidatec.wacare:id/textView_countryName")
		sleep(1)
		self.CT.click("com.lavidatec.wacare:id/tv_login")        
		sleep(2)
	def testThree(self):#帳號密碼錯誤
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		sleep(1)
		self.EC.enter("#","com.lavidatec.wacare:id/et_phone_num")
		sleep(3)
		self.find_Toast2("密碼須為6位以上")
		self.EC.enter("abcdefghij", "com.lavidatec.wacare:id/et_login_pass")
		sleep(1)
		self.CT.click("com.lavidatec.wacare:id/tv_login")        
		sleep(10)
	def testFour(self):#密碼不足六位
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		sleep(1)
		self.EC.enter("#","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("ji", "com.lavidatec.wacare:id/et_login_pass")
		sleep(1)
		self.CT.click("com.lavidatec.wacare:id/tv_login")        
		sleep(2)
	def testFive(self):#手機不曾註冊
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		sleep(1)
		self.EC.enter("#1540331","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("#", "com.lavidatec.wacare:id/et_login_pass")
		sleep(1)
		self.CT.click("com.lavidatec.wacare:id/tv_login")        
		sleep(2)



