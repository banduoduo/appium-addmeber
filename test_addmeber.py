# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker


class TestAddMeber():
    def setup_class(self):
        self.faker = Faker('zh-CN')

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = "launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(4)


    def teardown(self):
        self.driver.quit()

    def test_addmeber(self):
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()

        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//android.widget.EditText').send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')








