from page.Base import BasePage
from page.Locators.MD_Locators import DM_Locators


class Data_Matching(BasePage):
    # Open Data Matching page
    def open_site(self):
        self.go_to_url('https://data-matching.elis.rossum.ai/upload-companies')

    # Provides text from title Data Matching
    def title_present(self):
        return self.get_text(DM_Locators.TITLE_DM)

    # Open Upload Master Tab
    def open_upload_master(self):
        self.hover(DM_Locators.FIRST_TAB)
        self.click(DM_Locators.FIRST_TAB)

    # Open Setup a matching field Tab
    def open_setup_matching(self):
        self.hover(DM_Locators.SECOND_TAB)
        self.click(DM_Locators.SECOND_TAB)

    # Open Create matching logic Tab
    def open_create_matching_logic(self):
        self.hover(DM_Locators.THIRD_TAB)
        self.click(DM_Locators.THIRD_TAB)

    # Open Remove extension Tab
    def open_remove_extension(self):
        self.hover(DM_Locators.FOURTH_TAB)
        self.click(DM_Locators.FOURTH_TAB)

    # Execute logout
    def logout(self):
        self.hover(DM_Locators.LOGOUT)
        self.click(DM_Locators.LOGOUT)

    def is_first_tab_present(self):
        return self.is_element_present(DM_Locators.FIRST_TAB)

    def is_second_tab_present(self):
        return self.is_element_present(DM_Locators.SECOND_TAB)

    def is_third_tab_present(self):
        return self.is_element_present(DM_Locators.THIRD_TAB)

    def is_fourth_tab_present(self):
        return self.is_element_present(DM_Locators.FOURTH_TAB)

    def is_logout_present(self):
        return self.is_element_present(DM_Locators.LOGOUT)

    def is_sample_loc_json_present(self):
        return self.is_element_present(DM_Locators.SAMPLE_LOC_JSON)

    def is_sample_loc_xlsx_present(self):
        return self.is_element_present(DM_Locators.SAMPLE_LOC_XLSX)

    def is_sample_loc_csv_present(self):
        return self.is_element_present(DM_Locators.SAMPLE_LOC_CSV)

    def is_sample_po_present(self):
        return self.is_element_present(DM_Locators.SAMPLE_PO)

    def is_sample_schema_json_present(self):
        return self.is_element_present(DM_Locators.SAMPLE_SCHEMA_JSON)

    def is_sample_schema_xsd_present(self):
        return self.is_element_present(DM_Locators.SAMPLE_SCHEMA_XSD)

    def is_upload_button_not_clickable(self):
        return self.is_not_clickable(DM_Locators.UPLOAD_BUTTON)

    def is_upload_button_clickable(self):
        return self.is_clickable(DM_Locators.UPLOAD_BUTTON)

    def if_file_loaded(self):
        return self.is_element_present(DM_Locators.DONE)

    def file_error(self):
        return self.is_element_present(DM_Locators.ERROR_FILE)

    # Click on "Read More" button
    def open_read_more(self):
        self.hover(DM_Locators.READ_MORE)
        self.click(DM_Locators.READ_MORE)

    # Fill in Dataset field "DanilCompany"
    def specify_name(self):
        self.type(DM_Locators.DATA_SET_INPUT, 'DanilCompany')

    # Leave Dataset field empty
    def specify_empty_name(self):
        self.type(DM_Locators.DATA_SET_INPUT, '')

    # Choose and add file "JSON"
    def upload_file(self):
        self.upload(DM_Locators.CHOOSE_FILE_BUTTON, '/Users/bazucer/Desktop/IT/Rossum/sample_companies_2.json')

    # Choose and add file "JPG"
    def upload_jpg_file(self):
        self.upload(DM_Locators.CHOOSE_FILE_BUTTON, '/Users/bazucer/Desktop/IT/Rossum/rossum.jpg')

    # Click on encoding Dropdown box
    def encoding(self):
        self.hover(DM_Locators.DROPDOWN)
        self.click(DM_Locators.DROPDOWN)

    # Choose from encoding Dropdown box "UTF-8"
    def encoding_utf_8(self):
        self.hover(DM_Locators.DROPDOWN)
        self.click(DM_Locators.DROPDOWN)
        self.click(DM_Locators.UTF_8)

    # Choose from encoding Dropdown box "Windows-1250"
    def encoding_windows_1250(self):
        self.hover(DM_Locators.DROPDOWN)
        self.click(DM_Locators.DROPDOWN)
        self.click(DM_Locators.WINDOWS_1250)

    # Choose from encoding Dropdown box "Windows-1252"
    def encoding_windows_1252(self):
        self.hover(DM_Locators.DROPDOWN)
        self.click(DM_Locators.DROPDOWN)
        self.click(DM_Locators.WINDOWS_1252)

    # Choose from encoding Dropdown box "UTF-8-sig"
    def encoding_utf_8_sig(self):
        self.hover(DM_Locators.DROPDOWN)
        self.click(DM_Locators.DROPDOWN)
        self.click(DM_Locators.UTF_8_SIG)

    # Fill in Unique Identifier in Uploaded Data field "Supplier ID"
    def define_name_of_column(self):
        self.type(DM_Locators.UNIQUE_IDENTIFIER, 'Supplier ID')

    # Leave Unique Identifier field empty
    def define_empty_name_of_column(self):
        self.type(DM_Locators.UNIQUE_IDENTIFIER, '')

    # Click on "Upload file" button
    def upload_document(self):
        self.click(DM_Locators.UPLOAD_BUTTON)

    # Use for parametrized test in Dataset field
    def input_test_phrase_dataset(self, phrase: str):
        self.type(DM_Locators.DATA_SET_INPUT, phrase)

    # Use for parametrized test in Unique Identifier field
    def input_test_phrase_identifier(self, phrase: str):
        self.type(DM_Locators.UNIQUE_IDENTIFIER, phrase)
