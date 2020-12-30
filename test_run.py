import Pattern_Matching as hp


class main_run:

    def __init__(self, input_file):
        self.input_file = input_file

    def call_function(self):
        valid_ip_list = []
        valid_email_list = []
        valid_domain_list = []
        valid_url_list = []
        try:
            file_obj = hp.parse_file(self.input_file)
            file_data = file_obj.check_valid_file()
            for data in file_data:
                valid_obj = hp.validate_data(data)
                valid_ip = valid_obj.is_ip_of_valid_class()
                if valid_ip is not None: valid_ip_list.extend(valid_ip)
                valid_email_address = valid_obj.valid_email()
                if valid_email_address is not None: valid_email_list.extend(valid_email_address)
                valid_domain_name = valid_obj.valid_domain()
                if valid_domain_name is not None: valid_domain_list.extend(valid_domain_name)
                valid_url = valid_obj.valid_url_on_internet()
                if valid_url is not None: valid_url_list.extend(valid_url)
            print("valid_ip_list:", valid_ip_list)
            print("valid_email:", valid_email_list)
            print("valid_domain:", valid_domain_list)
            print("valid_url_list:", valid_url_list)
            extract_obj = hp.extract_ouput(valid_url_list)
            extracted_url_list = extract_obj.get_url_component()
            print("valid_url_list:", extracted_url_list)

        except TypeError:
            pass


if __name__ == '__main__':
    input_file = "test_html.txt"
    run_obj = main_run(input_file)
    run_obj.call_function()
