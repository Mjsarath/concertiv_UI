class CalculateSavingsPageConstants:
    VENDOR_NAME = "Market Data"
    ESTIMATE_VALUE = "//div/h3[contains(text(),'{value}')]/ancestor::div[2]//span[@class='cc__formula-result-value']"
    BASE_CASE_SAVINGS_LABEL = "Base Case Savings Estimate"
    TOP_SPEND_LABEL = "Top Side Spend Estimate"
    PROFESSIONAL_FIRM_INPUT = 50
    SLIDER_VALUE = "288" # equvalent value for 50 pixel input
    VENDOR_CHECKBOX = "//label[contains(text(),'{value}')]/parent::div/input[contains(@class,'Checkbox__Input')]"
