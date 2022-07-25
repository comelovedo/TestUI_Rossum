from page.data_matching import Data_Matching
from page.Registration import Login_Page
from conftest import generate_string, russian_chars, chinese_chars, special_chars
import pytest


def test_login(page):
    """ Positive test, Log in with valid account and password"""
    login = Login_Page(page)
    # Authorisation with valid account and password
    login.login_valid_account()
    matching_page = Data_Matching(page)
    # Check if on the Data Matching page
    assert "Data Matching" in matching_page.title_present()


def test_login_with_invalid_data(page):
    """Negative test, Log in with invalid account and password"""
    login = Login_Page(page)
    # Authorisation with invalid account and password
    login.login_invalid_account()
    matching_page = Data_Matching(page)
    # Check if not on the Data Matching page
    assert "Data Matching" not in matching_page.title_present()


def test_upload_document(page):
    """Positive test, fill all fields and upload correct file"""
    matching_page = Data_Matching(page)
    # Authorisation
    login = Login_Page(page)
    login.login_valid_account()
    # Fill in Dataset field "DanilCompany"
    matching_page.specify_name()
    # Choose and add file "JSON"
    matching_page.upload_file()
    # Fill in Unique Identifier in Uploaded Data field "Supplier ID"
    matching_page.define_name_of_column()
    # Click on "Upload file" button
    matching_page.upload_document()
    # Check if pop up "Done" is present
    assert matching_page.if_file_loaded() == True


def test_upload_with_jpg_file(page):
    """Negative test, fill all fields and upload incorrect file JPG"""
    matching_page = Data_Matching(page)
    # Authorisation
    login = Login_Page(page)
    login.login_valid_account()
    # Fill in Dataset field "DanilCompany"
    matching_page.specify_name()
    # Choose and add file "JPG"
    matching_page.upload_jpg_file()
    # Fill in Unique Identifier in Uploaded Data field "Supplier ID"
    matching_page.define_name_of_column()
    # Click on "Upload file" button
    matching_page.upload_document()
    # Check if pop up "File Error" is present
    assert matching_page.file_error() == True


def test_upload_document_without_dataset(page):
    """Negative test, upload correct file with empty field Dataset"""
    matching_page = Data_Matching(page)
    # Authorisation
    login = Login_Page(page)
    login.login_valid_account()
    # Leave Dataset field empty
    matching_page.specify_empty_name()
    # Choose and add file "JSON"
    matching_page.upload_file()
    # Fill in Unique Identifier in Uploaded Data field "Supplier ID"
    matching_page.define_name_of_column()
    # Check if Upload Button is not clickable
    assert matching_page.is_upload_button_not_clickable() == True


def test_upload_document_without_identifier(page):
    """Negative test, upload correct file with empty field Unique Identifier"""
    matching_page = Data_Matching(page)
    # Authorisation
    login = Login_Page(page)
    login.login_valid_account()
    # Fill in Dataset field "DanilCompany"
    matching_page.specify_empty_name()
    # Choose and add file "JSON"
    matching_page.upload_file()
    # Check if Upload Button is not clickable
    assert matching_page.is_upload_button_not_clickable() == True


@pytest.mark.parametrize("filter",
                         [
                             generate_string(255)
                             , generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , 123
                         ],
                         ids=
                         [
                             '255 symbols'
                             , 'more than 1000 symbols'
                             , 'russian'
                             , 'RUSSIAN'
                             , 'chinese'
                             , 'specials'
                             , 'digit'
                         ])
def test_upload_with_invalid_dataset(page, filter):
    """Negative test, upload correct file with different fill in Dataset, use parametrized test:
    255 symbols string,
    string > 1000 symbols,
    Cyrillic,
    UPPER CYRILLIC,
    Chinese symbols,
    Special chars,
    Digit.
    """
    matching_page = Data_Matching(page)
    # Authorisation
    login = Login_Page(page)
    login.login_valid_account()
    # Fill in Dataset field from "filter"
    matching_page.input_test_phrase_dataset(filter)
    # Choose and add file "JSON"
    matching_page.upload_file()
    # Fill in Unique Identifier in Uploaded Data field "Supplier ID"
    matching_page.define_name_of_column()
    # Click on "Upload file" button
    matching_page.upload_document()
    # Check if pop up "Done" not is present
    assert matching_page.if_file_loaded() == False


@pytest.mark.parametrize("filter",
                         [
                             generate_string(255)
                             , generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , 123
                         ],
                         ids=
                         [
                             '255 symbols'
                             , 'more than 1000 symbols'
                             , 'russian'
                             , 'RUSSIAN'
                             , 'chinese'
                             , 'specials'
                             , 'digit'
                         ])
def test_upload_with_invalid_identifier(page, filter):
    """Negative test, upload correct file with different fill in Unique Identifier, use parametrized test:
        255 symbols string,
        string > 1000 symbols,
        Cyrillic,
        UPPER CYRILLIC,
        Chinese symbols,
        Special chars,
        Digit.
        """
    matching_page = Data_Matching(page)
    # Authorisation
    login = Login_Page(page)
    login.login_valid_account()
    # Fill in Dataset field "DanilCompany"
    matching_page.specify_name()
    # Choose and add file "JSON"
    matching_page.upload_file()
    # Fill in Unique Identifier field from "filter"
    matching_page.input_test_phrase_identifier(filter)
    # Click on "Upload file" button
    matching_page.upload_document()
    # Check if pop up "Done" not is present
    assert matching_page.if_file_loaded() == False
