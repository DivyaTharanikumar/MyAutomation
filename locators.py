from selenium.webdriver.common.by import By

# for maintainability we can separate web objects by page name

class MainPageLocatars(object):
  LOGO          = (By.ID, 'nav-logo')
  ACCOUNT       = (By.ID, 'nav-link-accountList')
  SIGNUP        = (By.PARTIAL_LINK_TEXT, 'Start here')
  LOGIN         = (By.PARTIAL_LINK_TEXT,'Sign in')
  SEARCH        = (By.ID, 'twotabsearchtextbox')
  SEARCH_LIST   = (By.PARTIAL_LINK_TEXT,'Nexus 5')

class LoginPageLocatars(object):
  EMAIL         = (By.ID, 'ap_email')
  CONTINUE      = (By.ID, 'continue')
  PASSWORD      = (By.ID, 'ap_password')
  SUBMIT        = (By.ID, 'signInSubmit')
  ERROR_MESSAGE = (By.ID, 'auth-error-message-box')