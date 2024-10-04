from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the dynamic webpage
driver.get("https://v2.researchgiant.com/")  # Replace with the actual URL

# Wait for JavaScript to load (use WebDriverWait if needed)
driver.implicitly_wait(10)

# Extract the dynamic content (e.g., grabbing a specific element by class name)
element = driver.find_element(By.CLASS_NAME, "banner-content-wrapper")  # Replace with actual class or element

# Print or process the text
print(element.text)

# Close the browser
driver.quit()
