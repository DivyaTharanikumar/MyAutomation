from selenium.webdriver.common.by import By

# for maintainability we can separate web objects by page name

class MainPageLocators(object):
  LOGO          = (By.ID, 'nav-logo')
  ACCOUNT       = (By.ID, 'nav-link-accountList')
  SIGNUP        = (By.LINK_TEXT, 'Start here')
  LOGIN         = (By.LINK_TEXT,'Sign in')
  SEARCH        = (By.ID, 'twotabsearchtextbox')
  SEARCH_LIST   = (By.LINK_TEXT,'lenovo')

class LoginPageLocators(object):
  EMAIL         = (By.ID, 'ap_email')
  PASSWORD      = (By.ID, 'ap_password')
  SUBMIT        = (By.ID, 'signInSubmit')
  ERROR_MESSAGE = (By.ID, 'auth-error-message-box')
