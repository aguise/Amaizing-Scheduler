import json
import time
import requests

class ScheduleApiError(Exception):
    '''
    Raised if there is an error with the schedule API.
    '''
    pass

# The base API endpoint
base_url = 'http://umich-schedule-api.herokuapp.com/v4'

# the amount of time to wait for the schedule API
timeout_duration = 25

def get_data(relative_path):
    '''
    Gets data from the schedule API at the specified path.
    Will raise a ScheduleApiError if unsuccessful.
    Assumes API will return JSON, returns as a dictionary.
    '''

    timeout_at = time.time() + timeout_duration

    while time.time() < timeout_at:
        r = requests.get(base_url + relative_path)
        if r.status_code == 200:
            return json.loads(r.text)
        if r.status_code == 400:
            break

    raise ScheduleApiError('error for url: {0} message: "{1}" code: {2}' \
        .format(relative_path, r.text, r.status_code))

def get_terms():
    '''
    Returns a list of valid terms.
    Each item in the list is a dictionary containing:
        ('TermCode', 'TermDescr', 'TermShortDescr')
    '''
    return get_data('/get_terms')

'''pyt
You should add more functions below to get information from the API.

    -   In addition to the information provided in the spec, use the get_terms function 
        above as a model for how you might setup the other functions.
    -   Note some functions will need to have arguments (whereas get_terms does not).
    -   You may remove this comment when you start.
'''

def get_schools(TermCode):
    # concantenate url with termcode to return to get_data
    relative_path = '/get_schools?term_code=' + str(TermCode)

    return get_data(relative_path)

def get_subjects(TermCode,SchoolCode):
    # concantenante url with termcode + schoolcode to get_data
    url = ['/get_subjects?term_code=' +  str(TermCode), 'school=' + str(SchoolCode)]

    relative_path = '&'.join(url) 

    return get_data(relative_path)

def get_catalog_numbers(TermCode,SchoolCode,subject):
    # concatenate url with termcode + schoolcode + subject to get_data
    url = ['/get_catalog_numbers?term_code=' +  str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject)]

    relative_path = '&'.join(url)

    return get_data(relative_path)

def get_course_description(TermCode,SchoolCode,subject,catalog_num):
    # concatenate to get course description
    url = ['/get_course_description?term_code=' + str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject), 'catalog_num=' + str(catalog_num)]

    relative_path = '&'.join(url)

    return get_data(relative_path)

def get_additional_info(TermCode,SchoolCode,subject,catalog_num):
    # concatenate to get additional info
    url = ['/get_additional_info?term_code=' + str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject), 'catalog_num=' + str(catalog_num)]

    relative_path = '&'.join(url)
    
    return get_data(relative_path)

def get_sections(TermCode,SchoolCode,subject,catalog_num):
    # concatenate to get sections
    url = ['/get_sections?term_code=' + str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject), 'catalog_num=' + str(catalog_num)]

    relative_path = '&'.join(url)
    
    return get_data(relative_path)

def get_section_details(TermCode,SchoolCode,subject,catalog_num,sections):
    # concatenate to get specific section details
    url = ['/get_section_details?term_code=' + str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject), 'catalog_num=' + str(catalog_num), 'section_num=' + str(sections)]

    relative_path = '&'.join(url)
    
    return get_data(relative_path)

def get_meetings(TermCode,SchoolCode,subject,catalog_num,sections):
    # concatenate to get meetings
    url = ['/get_meetings?term_code=' + str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject), 'catalog_num=' + str(catalog_num), 'section_num' + str(sections)]

    relative_path = '&'.join(url)
    
    return get_data(relative_path)

def get_course_description_html(TermCode,SchoolCode,subject,catalog_num):
    # concatenate to get meetings
    url = ['/get_course_description_html?term_code=' + str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject), 'catalog_num=' + str(catalog_num)]

    relative_path = '&'.join(url)
    
    return get_data(relative_path)

def get_additional_info_html(TermCode,SchoolCode,subject,catalog_num):
    # concatenate to get meetings
    url = ['/get_additional_info_html?term_code=' + str(TermCode), 'school=' + str(SchoolCode), 'subject=' + str(subject), 'catalog_num=' + str(catalog_num)]

    relative_path = '&'.join(url)
    
    return get_data(relative_path)

