from Pages.locators import Module1Locators
from Pages.base_page import BasePage

class Module1Page(BasePage):
    def validate_element(self):
        return self.wait_for_element(Module1Locators.SOME_ELEMENT)

from Pages.locators import Module2Locators

class Module2Page(BasePage):
    def validate_element(self):
        return self.wait_for_element(Module2Locators.ANOTHER_ELEMENT)
