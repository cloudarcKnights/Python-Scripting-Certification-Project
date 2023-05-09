# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.indeed.com/jobs?q=GCP+cloud&l=Irvine%2C+CA&explvl=entry_level'
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')

# for job in job_listings:
#     title = job.find('a', class_='jobtitle').text.strip()
#     link = 'https://www.indeed.com' + job.find('a')['href']
#     print(title, link)

import requests

api_key = 'YOUR_API_KEY'  # Replace with your Google Jobs API key

base_url = 'https://jobs.googleapis.com/v1/'

# Set parameters for job search
params = {
    'key': api_key,
    'query': 'Cloud engineer entry level',
    'location': 'Irvine'
}

# Make API call to search for jobs
response = requests.get(base_url + 'jobs', params=params)

# Extract job results from response
jobs = response.json().get('jobResults')

# Print job details
for job in jobs:
    print(job.get('title'))
    print(job.get('companyName'))
    print(job.get('jobLocation').get('address').get('formattedAddress'))
    print(job.get('description'))
    print('---')
