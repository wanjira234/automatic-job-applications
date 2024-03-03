import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

USERNAME = "eppydev21@gmail.com"
PASSWORD = "Wanjira@21"
PHONE_NUMBER = "0703687201"


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3828590165&f_LF=f_AL&geoId=102257491&keywords=python"
           "%20developer&location=London%2C%20England%2C%20United%20Kingdom")
# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# sign-up button
time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value='//a[text()="Sign in"]')
sign_in_button.click()
# sign-in
time.sleep(5)
email = driver.find_element(By.ID, value="username")
email.send_keys(USERNAME, Keys.ENTER)
password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)

# If application requires phone number and the field is empty, then fill in the number.
# time.sleep(5)
# phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
# if not phone.get_attribute("value"):
#     phone.send_keys(PHONE_NUMBER)
#
# # Submit the application
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
# submit_button.click()
#
# time.sleep(5)
# Add a delay to ensure the application is submitted before quitting
# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

driver.quit()
