from selenium.webdriver.common.by import By


class CalculateSavingsLocators:
    CALCULATOR_CLASS = (By.CLASS_NAME, 'calculator')
    PROFESSIONAL_FIRM_COUNT = (By.CLASS_NAME, 'Range__Input-sc-7bfc0dd1-0')
    MARKET_DATA_VENDOR = (By.CLASS_NAME, 'cc__radio-question-item')
    ESTIMATE_VALUE = \
        (By.XPATH,
         "//div/h3[contains(text(),'{estimate_name}')]/ancestor::div[2]//span[@class='cc__formula-result-value']")
    UPDATED_FIRM_COUNT = (By.XPATH, "//h4[contains(@class,'RangeSlider__RangeResult')]")
    VENDOR_CHECKBOX = \
        (By.XPATH, "//label[contains(text(),'Market Data')]/parent::div/input[contains(@class,'Checkbox__Input')]")