# JobDarJob

In today's competitive job market, navigating the vast landscape of online job postings can be a daunting and time-consuming task. Job seekers often face the challenge of manually searching through numerous websites, sifting through irrelevant information, and struggling to compare opportunities across different platforms. This open-source project aims to address these challenges by providing a comprehensive and user-friendly solution that revolutionizes the job hunting experience.

At its core, this project serves as a powerful tool that aggregates job information from a wide range of online sources. Leveraging sophisticated web scraping techniques, the project meticulously extracts job details from various websites, ensuring that the information is accurate, up-to-date, and consistent. This meticulously curated data is then processed and transformed into a structured format, making it easily searchable and analyzable.

To further enhance the job hunting experience, the project presents the processed information through a user-friendly Telegram channel. This innovative approach eliminates the need for job seekers to visit multiple websites and provides a centralized location where they can effortlessly browse through relevant opportunities. The Telegram channel offers a streamlined interface that enables users to easily search, filter, and save job postings based on their specific criteria.

Moreover, the project goes beyond simply presenting job information; it empowers users to stay informed about new opportunities that align with their interests. By subscribing to the Telegram channel, users can receive real-time notifications whenever new job postings matching their search criteria become available. This proactive approach ensures that job seekers never miss out on potential opportunities that could be a perfect fit for their skills and aspirations.

****** 

### The project is divided into three distinct phases:

* Phase 1 : Web Scraping with Scrapy
In this phase, Scrapy, a powerful web scraping framework, will be utilized to extract job information from various job websites. Custom scrapers will be designed and implemented for each website to efficiently collect job details such as job title, description, requirements, salary, and contact information.

* Phase 2 : Telegram Bot Creation
In this phase, a functional Telegram bot will be built using the Telegram Bot API. This bot will allow users to access and easily search and filter the job information gathered in Phase 1. The bot can automatically notify users about new job opportunities that match their search criteria.

* Phase 3 : API Development with FastAPI
In this phase, a robust and user-friendly RESTful API will be constructed using FastAPI. This API will enable developers and third-party applications to programmatically access and process the collected job information.


******  

### Technologies
This project utilizes a combination of powerful technologies to achieve its goals:

* Poetry: A Python package manager for dependency management.
* Scrapy: A robust web scraping framework for extracting data from websites.
* MongoDB: A NoSQL database for storing and managing unstructured data.
* FastAPI: A high-performance web framework for building APIs.
* Pydantic: A data validation library for ensuring data integrity.
* Pytest: A comprehensive testing framework for unit and integration tests.


******* 
**Installation** 

1. To set up the project and its dependencies, follow these steps:

    ```bash
    git clone https://github.com/mohammadrezasolo69/JobDarJob.git
    ```

2. Install dependencies:

    ```bash
    poetry install
    ```