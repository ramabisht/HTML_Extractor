import unittest
import Pattern_Matching as pm


class TestCases(unittest.TestCase):
    def test_valid_file_location(self):
        valid_obj_file_true = pm.parse_file("test_html.txt")
        result = valid_obj_file_true.check_valid_file()
        self.assertNotEqual(result, None)

    def test_notvalid_file_location(self):
        valid_obj_file_false = pm.parse_file("test_html_1.txt")
        result = valid_obj_file_false.check_valid_file()
        self.assertEqual(result, None)

    def test_valid_ip(self):
        valid_obj_ip_true = pm.validate_data("20.0.0.0")
        result = valid_obj_ip_true.is_ip_of_valid_class()
        self.assertNotEqual(result, None)

    def test_notvalid_ip(self):
        valid_obj_ip_true = pm.validate_data("278.0000.0.0")
        result = valid_obj_ip_true.is_ip_of_valid_class()
        self.assertEqual(result, None)

    def test_valid_url(self):
        valid_obj_url_ture = pm.validate_data("https://www.google.com/")
        result = valid_obj_url_ture.valid_url_on_internet()
        self.assertNotEqual(result, None)

    def test_notvalid_url(self):
        valid_obj_url_false = pm.validate_data("htt://www.test.com/")
        result = valid_obj_url_false.valid_url_on_internet()
        self.assertEqual(result, None)

    def test_valid_domian(self):
        valid_obj_domain_ture = pm.validate_data("://www.google.com/")
        result = valid_obj_domain_ture.valid_domain()
        self.assertNotEqual(result, None)

    def test_notvalid_domian(self):
        valid_obj_domain_false = pm.validate_data(".google.com/")
        result = valid_obj_domain_false.valid_domain()
        self.assertEqual(result, None)

    def test_valid_email(self):
        valid_obj_email_ture = pm.validate_data("test123@gmail.com")
        result = valid_obj_email_ture.valid_email()
        self.assertNotEqual(result, None)

    def test_notvalid_email(self):
        valid_obj_email_false = pm.validate_data(".google.com/")
        result = valid_obj_email_false.valid_email()
        self.assertEqual(result, None)

    def test_split_url(self):
        obj_extract_url = pm.extract_ouput("https://www.google.com/")
        result = obj_extract_url.get_url_component()
        self.assertNotEqual(result, None)


if __name__ == '__main__':
    unittest.main()
