class HomeLocators:
    """ Home Page web elements """
    signin_button_xpath = '//*[@class="login"]'
    page_header_xpath = '//*[@class="page-heading"]'


class AuthLocators:
    """ Authentication Page web elements """
    form_section_xpath = '//*[@id="create-account_form"]'
    email_input_field_xpath = '//*[@id="email_create"]'
    create_account_button = '//*[@id="SubmitCreate"]'
    error_message_xpath = '//*[@id="create_account_error"]'


class CreateLocators:
    """ Create Account Page web elements """
    create_account_form_xpath = '//*[@id="account-creation_form"]'
    mr_radio_xpath = '//*[@id="id_gender1"]'
    mrs_radio_xpath = '//*[@id="id_gender2"]'
    first_name_rq_xpath = '//*[@id="customer_firstname"]'
    last_name_rq_xpath = '// *[@id = "customer_lastname"]'
    email_rq_xpath = '//*[@id="email"]'
    password_rq_xpath = '//*[@id="passwd"]'
    first_name_auto_xpath = '//*[@id="firstname"]'
    last_name_auto_xpath = '//*[@id="lastname"]'
    address_rq_xpath = '// *[@id = "address1"]'
    city_rq_xpath = '// *[@id = "city"]'
    state_rq_select_xpath = '//*[@id="id_state"]'
    zip_rq_xpath = '//*[@id="postcode"]'
    country_rq_select_xpath = '// *[@id = "id_country"]'
    mobile_rq_xpath = '//*[@id="phone_mobile"]'
    address_alias_rq_xpath = '//*[@id="alias"]'
    register_button_xpath = '//*[@id="submitAccount"]'
    error_alert_xpath = '//*[@class="alert alert-danger"]'
    my_account_header = '//*[@id="center_column"]/h1'

    required_fields = {
        first_name_rq_xpath: 'Robin',
        last_name_rq_xpath: 'Hood',
        # email_rq_xpath: 'jj3.xz@123.ee',
        password_rq_xpath: '1q2w3e4r',
        first_name_auto_xpath: 'Robin',
        last_name_auto_xpath: 'Hood',
        address_rq_xpath: '220 S Union St',
        city_rq_xpath: 'Alexandria',
        state_rq_select_xpath: '46',
        zip_rq_xpath: '22314',
        mobile_rq_xpath: '5417543010'
    }

