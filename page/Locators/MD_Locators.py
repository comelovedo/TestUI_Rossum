class DM_Locators:
    """ Locators on Data Matching page"""

    # Title "Data Matching page"
    TITLE_DM = "text=Data Matching"
    # Navigation Tabs
    FIRST_TAB = 'text=Upload master data'
    SECOND_TAB = 'text=Set up a matching field'
    THIRD_TAB = 'text=Create matching logic'
    FOURTH_TAB = 'text=Remove extension'
    LOGOUT = 'text=Logout'

    # Read More Button
    READ_MORE = '[rel="noopener noreferrer"]'

    # Input Specify the name of the dataset
    DATA_SET_INPUT = '[placeholder=\"Enter name of the dataset\"]'

    # Button "Choose file" Select the file containing list of companies
    CHOOSE_FILE_BUTTON = 'input[type=\"file\"]'

    # Attached files
    SAMPLE_LOC_JSON = 'a:has-text(\"JSON\")'
    SAMPLE_LOC_XLSX = 'a:has-text(\"XLSX\")'
    SAMPLE_LOC_CSV = 'a:has-text(\"CSV\")'
    SAMPLE_PO = 'xpass=//a[@class="styles_SampleFormat__1CaUg"]'
    SAMPLE_SCHEMA_JSON = 'a:has-text(\"JSON\")'
    SAMPLE_SCHEMA_XSD = "text=XSD"

    # Dropdown box ro encoding
    DROPDOWN = '.ui-select__control'
    UTF_8 = '#react-select-14-option-0'
    WINDOWS_1250 = '#react-select-14-option-1'
    WINDOWS_1252 = '#react-select-14-option-2'
    LATINA_1 = '#react-select-14-option-3'
    UTF_8_SIG = '#react-select-14-option-4'

    # Input Unique Identifier in Uploaded Data
    UNIQUE_IDENTIFIER = '[placeholder=\"Fill in the column\\/element name\"]'

    # Button for uploading file
    UPLOAD_BUTTON = '[placeholder=\"Fill in the column\\/element name\"]'

    # Popup plates
    DONE = "#root div:has-text(\"DoneYour data is being processed. We will send you an email when it’s ready.\")"
    ERROR_FILE = "#root div:has-text(\"Error{'files': ['Invalid File Format: jpg.']}\")"