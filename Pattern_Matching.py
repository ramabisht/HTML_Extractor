import requests
import re
import ipaddress
from urllib.parse import urlparse
import logging


logging.basicConfig(level = logging.INFO, filename = 'pattern_matcher.log')
# Class to Parse the HTML file (test_html.txt) and extract data
class parse_file():
    def __init__(self, input_file):
        self.input_file = input_file

    def check_valid_file(self):
        try:
            with open(self.input_file, 'r') as html_file:
                read_output = html_file.readlines()
                logging.info(read_output)
                return read_output
        except IOError:
            return None


''' Class to extract the data from file
All valid URLs and domains.
Extract all Valid IP addresses, based upon different classes.
Extract all valid email addresses'''

class validate_data:

    def __init__(self, string_to_match):
        self.string_to_match = string_to_match

    def get_valid_ip_list(self):
        valid_ip_str_list = []
        valid_ip_str = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', self.string_to_match)
        if valid_ip_str:
            valid_ip_str_list.extend(valid_ip_str)
        return valid_ip_str_list

    def is_ip_of_valid_class(self):
        final_valid_ip_list = []
        valid_ip_str_list = validate_data.get_valid_ip_list(self)
        if len(valid_ip_str_list) > 0:
            try:
                final_valid_ip_list = list(map(lambda ip: ipaddress.ip_address(ip), valid_ip_str_list))
                if final_valid_ip_list:
                    final_valid_ip_list.extend(final_valid_ip_list)
            except ValueError:
                logging.info("Invalid class IP Found!")

        if len(final_valid_ip_list) > 0:
            return final_valid_ip_list

    def valid_url_string(self):
        final_url_list = []
        url_pattern_list = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.string_to_match)
        if url_pattern_list:
            final_url_list.extend(url_pattern_list)
        return final_url_list

    def valid_url_on_internet(self):
        url_list = []
        valid_url = self.valid_url_string()
        if len(valid_url) > 0:
            for url in valid_url:
                try:
                    requests.get(url)
                    url_list.append(url)
                    logging.info("this is valid URL on internet")
                except requests.ConnectionError as exception:
                    logging.info("This is not a valid url on internet")
            return url_list
        else:
            logging.info("This is not a valid url on internet")

    def valid_domain(self):
        valid_domain_list = []
        valid_domain = re.findall(r':?//(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.string_to_match)
        if valid_domain and len(valid_domain) > 0:
            valid_domain_list.extend(valid_domain)
            logging.info("This pattern is a valid domain")
            return valid_domain_list
        else:
            logging.info("This pattern is not a valid domain")

    def valid_email(self):
        final_email_list = []
        email_list = re.findall(r'[\w\.-]+@[\w\.-]+', self.string_to_match)
        if len(email_list) > 0:
            logging.info("a valid email address")
            final_email_list.extend(email_list)
        else:
            logging.info("not a valid email address")

        if len(final_email_list) > 0:
            return email_list


''' Class to extract the data from file
If it is a URL divide it into PROTOCOL, DOMAIN, URI PATH and Query String.
'''
class extract_ouput():
    def __init__(self, url_list):
        self.url_list = url_list
    def get_url_component(self):
        try:
            extracted_data = list(map(lambda url: urlparse(url), self.url_list))
            return extracted_data
        except TypeError:
            pass
