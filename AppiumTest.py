
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
action = TouchAction(driver)  # ativa os gestos

#driver.find_element_by_id('com.google.android.apps.nexuslauncher:id/all_apps_handle').click()
driver.find_element_by_accessibility_id('Play Store').click()

#procurar por Istagram
#driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]").click()
driver.implicitly_wait(5)
driver.press_keycode(37)            # letra i no teclado
driver.press_keycode(42)            # letra n teclado nativo

#driver.press_keycode(84)            # clica na busca
driver.execute_script('mobile: performEditorAction',{'action':'search'})

popbtn = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]')
popbtn.click()

install = driver.find_element_by_class_name('android.widget.Button')
install.click()

# ficou faltando um assert para o sucesso do DL




