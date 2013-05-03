""" Configurations and login settings to
    connect to glassdoor and scrape data
"""
LOGIN = True

HOST = {
    'base': 'http://www.glassdoor.com',
    'login': '/profile/login_input.htm?u=%2Findex.htm',
    }

USER = {
    'username': 'USERNAME',
    'password': 'PASSWORD',
    }

FORM_PARAMS = {
    'login': {
        # xpaths
        'username': "//input[@id='AuthEmail']",
        'password': "//input[@id='AuthPW']",
        'commands': {
            'selected': [
                '//*[@id="RememberMe"]',
                ],
            'submitted': [
                '//*[@id="LoginForm"]/div/button',
                ],
            },
        },
    }

QUERIES = [
    ("Salaries", "http://www.glassdoor.com/Salaries/index.htm"),
    ("Jobs", "http://www.glassdoor.com/Jobs/jobs.htm"),
    ]

COMMANDS ={
    'search':{
        "text": '//*[@id="SiteSearchTop"]/form/span/input[1]',
        "submit": '//*[@id="SiteSrchHome"]/div/div[3]/form/span/button',
        },
    "toolbar": '//*[@id="FooterPageNav"]/div[1]/ul',
    }

JOBS = [
    "Tableau",
    "Hadoop",
    "Big Data",
    "Data Scientist",
    "Data Analyst",
    "Data Architect",
    "Data Engineer",
    ]

JOB_TYPES = [
    "All Job Types",
    "Full-time",
    "Part-time",
    "Contract",
    "Internship",
    "Temporary",
    ]
