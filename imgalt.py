from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace with your webpage URL
URL = "https://www.jabercrombia.com"

# Set up Selenium WebDriver (Ensure chromedriver is in your PATH)
driver = webdriver.Chrome()

# Open the webpage
driver.get(URL)

# Find all <img> tags
images = driver.find_elements(By.TAG_NAME, "img")

# Check for missing or empty alt attributes
missing_alt = []
for img in images:
    alt_text = img.get_attribute("alt")
    if not alt_text:  # Checks if alt is missing or empty
        missing_alt.append(img.get_attribute("src"))  # Store image URL or source

# Output results
if missing_alt:
    print("❌ Images missing alt attributes:")
    for src in missing_alt:
        print(f"- {src}")
else:
    print("All images have alt attributes!")

# Close the browser
driver.quit()
