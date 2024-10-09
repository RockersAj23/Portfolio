# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service

# # service = Service(verbose = True)

# # driver = webdriver.Edge(service = service)

# # driver.get('https://bing.com')

# # element = driver.find_element(By.ID, 'sb_form_q')
# # search_q=['welcome','lets go','we will']


# # for i in search_q:
# #     element.send_keys(i)

# # element.submit()

# # time.sleep(20)
# # driver.quit()

# from selenium.webdriver.common.keys import Keys
# import time

# # Function to perform Bing search
# def bing_search_in_new_tab(query, driver):
#     # Open a new tab
#     driver.execute_script("window.open('about:blank', '_blank');")
#     driver.switch_to.window(driver.window_handles[-1])

#     # Navigate to Bing
#     driver.get("https://www.bing.com")

#     # Find the search box and input the query
#     search_box = driver.find_element(By.ID, 'sb_form_q')
#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)

#     # Wait for results to load
#     time.sleep(10)

# # Predetermined searches
# search_queries = [
#     "query 66",
#     "query 67",
#     "query 68",
#     "query 69",
#     "query 70",
#     "query 71",
#     "query 72",
#     "query 73",
#     "query 74",
#     "query 75",
#     "query 76",
#     "query 77",
#     "query 78",
#     "query 79",
#     "query 80",
#     "query 81",
#     "query 82",
#     "query 83",
#     "query 84",
#     "query 85",
#     "query 86",
#     "query 87",
#     "query 88",
#     "query 89",
#     "query 90",
#     "query 91",
#     "query 92",
#     "query 93"
# ]

# # Initialize Microsoft Edge WebDriver
# driver = webdriver.Edge("A:\STUFF\edgedriver_win64\msedgedriver.exe") # Replace "path/to/msedgedriver.exe" with the actual path to your msedgedriver.exe

# # Perform searches in multiple tabs
# for query in search_queries:
#     bing_search_in_new_tab(query, driver)
#     time.sleep(10)  # Wait for 20 seconds before opening the next tab

# # Close the browser
# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time

# Location of Microsoft Edge WebDriver
edge_driver_path = "A:/STUFF/edgedriver_win64/msedgedriver.exe"

# Initialize Microsoft Edge WebDriver
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

# Function to perform Bing search in a new tab
def bing_search_in_new_tab(query, driver):
    # Open a new tab
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    # Navigate to Bing
    driver.get("https://www.bing.com")

    # Find the search box and input the query
    search_box = driver.find_element(By.ID, 'sb_form_q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(10)

# Predetermined searches
search_queries = [
    "query 66", "query 67", "query 68", "query 69", "query 70", 
    "query 71", "query 72", "query 73", "query 74", "query 75",
    "query 76", "query 77", "query 78", "query 79", "query 80", 
    "query 81", "query 82", "query 83", "query 84", "query 85", 
    "query 86", "query 87", "query 88", "query 89", "query 90", 
    "query 91", "query 92", "query 93"
]

# Perform searches in multiple tabs
for query in search_queries:
    bing_search_in_new_tab(query, driver)
    time.sleep(10)  # Wait for 10 seconds before opening the next tab

# Close the browser after all searches are done
driver.quit()
