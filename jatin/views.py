# Import necessary modules and models
from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from .models import Property  # Import your Property model

def scrape_properties_view(request):
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the website
    url = "https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R"
    driver.get(url)

    # Add a delay to wait for elements to load (adjust the sleep duration as needed)
    time.sleep(5)  # Wait for 5 seconds (you can increase or decrease this)

    # Find all elements with the specified class names and get their attributes
    elements = driver.find_elements(By.CLASS_NAME, "projectTuple__projectName")
    links = [element.get_attribute("href") for element in elements]

    # Initialize empty lists to store data
    building_types = []
    prices = []
    property_names = []
    areas = []
    localities = []

    # Loop through the links and open each details page in a new tab or window
    for link in links:
        driver.execute_script(f"window.open('{link}', '_blank');")
        # Switch to the newly opened tab or window
        driver.switch_to.window(driver.window_handles[-1])

        # Add a delay to allow the details page to load (adjust the sleep duration as needed)
        time.sleep(3)

        # Scrape building type
        building_type = driver.find_element(By.CLASS_NAME, "ellipsis.list_header_semiBold.configurationCards__configurationCardsSubHeading").text

        # Scrape price
        price = driver.find_element(By.CLASS_NAME, "list_header_semiBold.configurationCards__configurationCardsHeading").text

        # Scrape property name
        property_name = driver.find_element(By.CSS_SELECTOR, ".ProjectInfo___99DeskProjTitle.pageComponent .ProjectInfo__imgBox1.title_bold").text

        # Scrape area
        area = driver.find_element(By.CLASS_NAME, "caption_subdued_medium.configurationCards__cardAreaSubHeadingOne").text

        # Scrape locality
        locality = driver.find_element(By.XPATH, '//*[@id="project-details"]/h1/span[2]/span').text

        # Append scraped data to respective lists
        building_types.append(building_type)
        prices.append(price)
        property_names.append(property_name)
        areas.append(area)
        localities.append(locality)

        # Create and save a Property object for each scraped property
        property = Property(
            name=property_name,
            cost=price,
            property_type=building_type,
            area=area,
            locality=locality,
            link=link
        )
        property.save()

        # Close the current tab or window
        driver.close()

        # Switch back to the main tab or window
        driver.switch_to.window(driver.window_handles[0])

    # Close the browser window when you're done
    driver.quit()

    return HttpResponse("Scraping completed!")  # Return a response indicating the completion of scraping
