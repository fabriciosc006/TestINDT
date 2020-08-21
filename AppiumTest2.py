from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

#capabilities
desired_cap = {
       "platformName": "Android",
       "platformVersion": "8.0",
       "deviceName": "Android Emulator"
}


driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap) # servidor do appium
driver.implicitly_wait(10)

driver.find_element_by_id('com.google.android.apps.nexuslauncher:id/all_apps_handle').click()
driver.find_element_by_accessibility_id('Instagram').click()                       #clicar no insta  p abir o app
#driver.find_element_by_id('com.instagram.android:id/log_in_button').click()        #clicar no login do insta


#driver.find_element_by_id('com.instagram.android:id/sign_up_with_email_or_phone').click()
#driver.find_element_by_id('com.instagram.android:id/log_in_button').click()

#joga para o campo de email e nao de phone
emailtype = driver.find_element_by_xpath("//android.widget.TextView[@text='EMAIL']").click()

email = str(input('Digite o seu endereco de e mail: ')).split()  #cliente digita senha
#psw = str(input('Digite a sua senha: ')).split()


emafield = driver.find_element_by_id('com.instagram.android:id/email_field')
driver.set_value(emafield,email)
driver.find_element_by_id('com.instagram.android:id/button_text').click()




