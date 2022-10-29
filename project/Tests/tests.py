import pytest
from framework.Driver.AlertUtils import AlertUtils
from framework.Driver.DriverUtils import DriverUtils
from framework.Utils.RandomUtils import RandomUtils
from project.Pages.AlertsFrameWindowsPage import AlertsFrameWidowsPage
from project.Pages.AlertsPage import AlertsPage
from project.Pages.BrowserWindowsPage import BrowserWindowsPage
from project.Pages.ElementsPage import ElementsPage
from project.Pages.FramesPage import FramesPage
from project.Pages.Homepage import Homepage
from project.Pages.LinksPage import LinksPage
from project.Pages.NestedFramesPage import NestedFramesPage
from project.Pages.NewTabPage import NewTabPage
from project.Pages.WebTablesPage import WebTablesPage
from framework.Utils.DataUser import DataUser
from framework.Utils.DataUtils import DataUtils
from framework.Utils.Logger import Logger
from framework.Driver.conftest import setup  # Need for the fixtures


@pytest.mark.usefixtures('setup')
class Test:

    def test_alerts(self):
        Logger.log_info("Start test_alerts")
        homepage = Homepage()
        assert homepage.is_form_open(), "Main page is NOT open"
        homepage.open_alerts_frame_windows()
        alert_frame_windows_page = AlertsFrameWidowsPage()
        assert alert_frame_windows_page.is_form_open(), "Alerts form is NOT open"
        alert_frame_windows_page.click_btn_alerts()
        alerts_page = AlertsPage()
        assert alerts_page.is_form_open(), "Alerts form is NOT open"
        alerts_page.click_btn_to_see_alert()
        assert AlertUtils.is_alert(), "Alert is NOT open"
        assert AlertUtils.get_alert_text() == (DataUtils.test_data_json()['alert_text']), \
            "Alert with text 'You clicked a button' is NOT open"
        AlertUtils.alert_accept()
        assert AlertUtils.is_alert() is False, "Alert has NOT closed"
        alerts_page.click_btn_to_confirm()
        assert AlertUtils.is_alert(), "Confirm alert is NOT open"
        assert AlertUtils.get_alert_text() == DataUtils.test_data_json()['confirm_text'], \
            "Alert with text 'Do you confirm action?' is NOT open"
        AlertUtils.alert_accept()
        assert AlertUtils.is_alert() is False, "Confirm alert has NOT closed"
        assert alerts_page.result_confirm_text() == DataUtils.test_data_json()['result_confirm_box_text'], \
            "Text 'You selected Ok' has appeared on page"
        alerts_page.click_btn_to_prompt()
        assert AlertUtils.is_alert(), "Prompt alert is NOT open"
        assert AlertUtils.get_alert_text() == DataUtils.test_data_json()['prompt_text'], \
            "Alert with text 'Please enter your name' is NOT open"
        random_text_to_prompt = RandomUtils.generate_random_text()
        AlertUtils.type_to_prompt(random_text_to_prompt)
        assert AlertUtils.is_alert() is False, "Prompt alert has NOT closed"
        assert alerts_page.result_prompt_text() == random_text_to_prompt, "Text does NOT equals to the entered before"

    def test_iframe(self):
        Logger.log_info("Start test_iframe")
        homepage = Homepage()
        assert homepage.is_form_open(), "Main page is NOT open"
        homepage.open_alerts_frame_windows()
        alert_frame_windows_page = AlertsFrameWidowsPage()
        assert alert_frame_windows_page.is_form_open(), "Alerts form is NOT open"
        alert_frame_windows_page.click_btn_nested_frames()
        nested_frames_page = NestedFramesPage()
        assert nested_frames_page.is_form_open(), "Alerts form has NOT appeared on page"
        assert nested_frames_page.is_nested_frames_form(), "Page with Nested Frames form is NOT open."
        nested_frames_page.switch_to_parent_frame()
        assert nested_frames_page.is_parent_frame() == DataUtils.test_data_json()["parent_frame_text"], \
            "Message 'Parent frame' does NOT present on page"
        nested_frames_page.switch_to_child_frame()
        assert nested_frames_page.is_child_frame() == DataUtils.test_data_json()["child_frame_text"], \
            "Message 'Child frame' does NOT present on page"
        DriverUtils.switch_to_default_frame()
        nested_frames_page.click_btn_frames()
        frame_page = FramesPage()
        assert frame_page.is_form_open(), "Page with Frames form is NOT open"
        frame_page.switch_to_upper_frame()
        frame_page.get_upper_frame_text()
        DriverUtils.switch_to_default_frame()
        frame_page.switch_to_lower_frame()
        frame_page.get_lower_frame_text()
        assert frame_page.get_upper_frame_text() == frame_page.get_lower_frame_text(), \
            "Message from upper frame is NOT equal to the message from lower frame"

    def test_tables(self):
        Logger.log_info("Start test_tables")
        homepage = Homepage()
        assert homepage.is_form_open(), "Main page is NOT open"
        homepage.open_elements()
        elements_page = ElementsPage()
        assert elements_page.is_form_open(), "Alerts form is NOT open"
        elements_page.click_btn_web_tables()
        web_tables_page = WebTablesPage()
        assert web_tables_page.is_form_open(), "Web Tables is NOT open"
        amount_users_before_add = web_tables_page.count_added_users()
        web_tables_page.click_btn_add()
        assert web_tables_page.is_reg_form(), "Registration form has NOT appeared on page"
        user_data = DataUser(*DataUtils.handling_data_for_table())
        web_tables_page.type_first_name(user_data.first_name)
        web_tables_page.type_last_name(user_data.last_name)
        web_tables_page.type_email(user_data.email)
        web_tables_page.type_age(user_data.age)
        web_tables_page.type_salary(user_data.salary)
        web_tables_page.type_department(user_data.department)
        web_tables_page.click_btn_submit()
        amount_users_after_add = web_tables_page.count_added_users()
        assert web_tables_page.is_reg_form() is False, "Registration form has NOT closed."
        assert amount_users_before_add != amount_users_after_add, "Number of records in table has NOT changed"
        assert set(user_data.get_set_full_info()) == web_tables_page.searching_user_data(
            DataUtils.handling_data_for_table()), \
            "Data of user has NOT appeared in a table"
        web_tables_page.delete_user(amount_users_after_add)
        amount_users_after_delete = web_tables_page.count_added_users()
        assert amount_users_after_delete != amount_users_after_add, "Number of records in table has NOT changed"

    def test_handles(self):
        Logger.log_info("Start test_handles")
        homepage = Homepage()
        assert homepage.is_form_open(), "Main page is NOT open"
        homepage.open_alerts_frame_windows()
        alert_frame_windows_page = AlertsFrameWidowsPage()
        assert alert_frame_windows_page.is_form_open(), "Alerts form is NOT open"
        alert_frame_windows_page.click_btn_browser_windows()
        browser_windows_page = BrowserWindowsPage()
        assert browser_windows_page.is_form_open(), "Page with Browser Windows form is NOT open"
        browser_windows_page.click_new_tab()
        DriverUtils.switch_to_last_tab()
        new_tab_page = NewTabPage()
        assert new_tab_page.is_form_open(), "New tab with sample page is NOT open"
        DriverUtils.close_current_tab()
        DriverUtils.switch_to_last_tab()
        assert browser_windows_page.is_form_open(), "Page with Browser Windows form is NOT open"
        browser_windows_page.click_btn_elements()
        browser_windows_page.click_btn_links()
        links_page = LinksPage()
        assert links_page.is_form_open(), "Page with Links form is NOT open"
        links_page.click_btn_home()
        DriverUtils.switch_to_last_tab()
        assert homepage.is_form_open(), "New tab with main page is NOT open"
        DriverUtils.switch_to_first_tab()
        assert links_page.is_form_open(), "Page with Links form is NOT open"
