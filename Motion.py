class swipePage():
	def __init__(self, driver):
		self.driver = driver
		self.screenWidth = driver.get_window_size()['width']
		self.screenHeight = driver.get_window_size()['height']
	def swipeUp(self, t=250, n=1):
		x1 = self.screenWidth * 0.5    
		y1 = self.screenHeight * 0.75   
		y2 = self.screenHeight * 0.1   
		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2, t)
	def swipeDown(self, t=250, n=1):
		x1 = self.screenWidth * 0.5         
		y1 = self.screenHeight * 0.1       
		y2 = self.screenHeight * 0.75        
		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2,t)
	def swipLeft(self, t=250, n=1):
		x1 = self.screenWidth * 0.75
		y1 = self.screenHeight * 0.5
		x2 = self.screenWidth * 0.1
		for i in range(n):
			self.driver.swipe(x1, y1, x2, y1, t)
	def swipRight(self, t=250, n=1):
		l = driver.get_window_size()
		x1 = self.screenWidth * 0.1
		y1 = self.screenHeight * 0.5
		x2 = self.screenWidth * 0.75
		for i in range(n):  
			self.driver.swipe(x1, y1, x2, y1, t)    

class enterContext():
	def __init__(self, driver):
		self.driver = driver
	def enter(self, context, resource_id):
		#testfiled = self.driver.find_elements_by_class_name("android.widget.EditText")
		testfiled = self.driver.find_element_by_id(resource_id)
		testfiled.send_keys(context)

class clickAndTap():
	def __init__(self, driver):
		self.driver = driver

	def tap(self, target):
		self.driver.tap(target)

	def click(self, resource_id):
		target = self.driver.find_element_by_id(resource_id)
		target.click()

# 目前已知選擇器 
		#  - find_element_by_accessibility_id
		#  id - find_element(s)_by_id
		#  class - find_element(s)_by_class_name
		#  name - find_element(s)_by_name
		#el = self.driver.find_element_by_accessibility_id("Add Contact")
		#el.click()
	   