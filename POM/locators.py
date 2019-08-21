__author__ = 'Alexey Koledachkin'

class Locator():

#/signup?marketing_tag=qa_test_Le8KzIP57Nf00Hbb

###   Social links   ###
    rss = "//i[@class='fa fa-rss-square']"
    youtube = "//i[@class='fa fa-youtube-square']"
    facebook = "//i[@class='fa fa-facebook-square']"
    twitter = "//i[@class='fa fa-twitter-square']"
###   Home page and Contact Us   ###
    logo = "//a[@title='Simple Toll-Free Logo']"
    sign_up = "//a[@title='Go to Sign Up Page']"
    login = "//div[@class='navbar-right hidden-xs']//a[@title='Log In']"

    home = "//header//a[@title='Go to Home Page']"
    contact_us = "//header//a[@title='Go to Contact Us Page']"
    faq = "//header//a[@title='Go to FAQs Page']"
    about_us = "//header//a[@title='Go to About Us Page']"
    tel = "//tel/span"

    home_bottom = "//footer//a[@title='Go to Home Page']"
    contact_bottom = "//footer//a[@title='Go to Contact Us Page']"
    faq_bottom = "//footer//a[@title='Go to FAQs Page']"
    about_bottom = "//footer//a[@title='Go to About Us Page']"

###   About Us   ###
    fcc = "//a[@title='FreeConferenceCall.Com']"
    fccBusiness = "//a[@title='FreeConferenceCall.com For Business']"

###   Contact Us   ###
    name = "//input[@name='name']"
    email = "//input[@name='email']"
    phone = "//input[@name='phone']"
    comments = "//textarea[@name='comments']"
    submit = "//button[@type='submit']"
    fcc_link = "//a[@title='FreeConferenceCall.Com']"
    r_field = "//li[text()='This value is required']"
    invalid_mail = "//li[text()='This value should be a valid email']"
    invalid_number = "//li[text()='This value length is invalid. It should be between 10 and 17 characters long']"

###   FAQs   ###
    submit_trouble = "//a[@title='Go to Trouble Ticket Page']"
    refer_friend = "//a[@title='Go to Refer a Friend Page']"
    instruction = "//a[@title='Go to Instructions Page']"


###   Submit Trouble Ticket   ###
    name_field = "//input[@id='name']"
    email_field = "//input[@id='email']"
    phone_number = "//input[@id='phonenumber']"
    contact_preference_email = "//input[@value='Email']"
    contact_preference_phone = "//input[@value='Phone']"
    conference_date = "//input[@id='confdate']"
    conference_time = "//input[@id='conftime']"
    dial_number = "//input[@name='dialin_number']"
    access_code = "//*[@id='access_code_forgot']"
    carrier = "//select[@name='carrier']" # SELECT
    phone_type = "//select[@name='phonetype']" # SELECT
    subject = "//select[@name='subject_type']" # SELECT
    details = "//textarea[@name='details']"

###   Refer a friend   ###
    friend_name = "//input[@name='friend_name']"
    friend_email = "//input[@name='friend_email']"
    your_name = "//input[@name='your_name']"
    your_email = "//input[@name='Your Email']"

###   Sign Up   ###
    first_name = "//input[@placeholder='First Name']"
    last_name = "//input[@placeholder='Last Name']"
    phone_num = "//input[@name='phonenumber']"
    company_name = "//input[@placeholder='Company Name']"
    card_type = "//select[@name='credit_card[payment]']" # SELECT
    card_number = "//input[@placeholder='Card Number']"
    mm = "//select[@name='credit_card[expiration_month]']" # SELECT
    yyyy = "//select[@name='credit_card[expiration_year]']" # SELECT
    cvv = "//input[@placeholder='CVV']"
    card_holder_name = "//input[@placeholder='Card Holder Name']"
    terms_conditions = "//input[@name='agree']"
    street_address = "//input[@placeholder='Street Address']"
    suite = "//input[@placeholder='Suite']"
    city = "//input[@placeholder='City']"
    state = "//select[@name='state']" # SELECT
    zip = "//input[@name='zip']"
    same_above = "//input[@name='billingsamecontact']"
    log_out = "//a[text()='Log out'][1]"


    SignUp_Toll = "/html/body/div[4]/div[1]/div[1]/div/div[2]/dl[2]/dd[1]"
    SignUp_Access = "/html/body/div[4]/div[1]/div[1]/div/div[2]/dl[2]/dd[3]"
    SignUp_PIN = "/html/body/div[4]/div[1]/div[1]/div/div[2]/dl[2]/dd[4]"




###   Email   ###
    pin_letter = "//*/table[3]/tbody/tr/td[2]/table/tbody/tr/td"

    test_login_email = "//input[@name='login']"
    test_submit_button = "//button[@type='submit']"
    test_password_email = "//input[@name='passwd']"

    checkbox_clear = "//span[@class='checkbox_view']"
    delete = "//span[text()='Удалить']"

    thank_you = "//h1[text()='Thank you for signing up with SimpleTollFree']"

    email_access_code = "//table[2]/tbody/tr/td[2]/table/tbody/tr/td"
    email_host_pin = "//table[3]/tbody/tr/td[2]/table/tbody/tr/td"
    email_number = "//table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/a/span"

    prof_state_locator = "//select[@name='subscription[state]']/option[@value='Arizona']"

###   Login   ###
    host_pin = "//input[@name='subscriber_pin']"
    remember_me = "//input[@name='rememberme']"
    accesscode = "//input[@name='access_code']"

    page_name = "//h1[text()='Account Information']"
    forgot_pass = "//a[@id='forgot_pin']"
    send_info = "//button[text()='Send Info']"

    alert = "//span[text()='Your account info has been emailed to smcallacc@gmail.com']"

###   Account information   ###
    Toll = "//dd[1]"

    TollFree = "//dd[2]"
    acc_AccessCode = "//dd[3]"
    acc_HostPIN = "//dd[4]"

    acc_Playback_number = "//dd[5]"

    acc_email = "//input[@name='subscription[email]']"
    acc_first_name = "//input[@placeholder='First Name']"
    acc_last_name = "//input[@placeholder='Last Name']"
    acc_phone_num = "//input[@placeholder='Phone Number']"
    acc_company_name = "//input[@placeholder='Company Name']"

    acc_street_address = "//input[@placeholder='Street Address']"
    acc_suite = "//input[@placeholder='Suite']"
    acc_city = "//input[@placeholder='City']"
    acc_state = "//select[@name='subscription[state]']" # SELECT
    acc_zip = "//input[@placeholder='Zip']"

    acc_timezones = "//select[@id='timezones']"
    acc_change_zones = "//button[@id='toggle-tz']"
    acc_resend_info = "//button[text()='Resend Info']"
    resend_info_message = "//span[text()='Information has been resend successfully']"


###   History and recordings   ###

    start_date = "//input[@placeholder='Start Date']"
    end_date = "//input[@placeholder='End Date']"
    type_conference = "//select[option]"
    search = "//button[text()='Search']"

    ### Sorting
    sort_by_date_time = "//div[text()='Start Date/Time']"
    sort_by_end_time = "//div[text()='End Time']"
    sort_by_callers = "//div[text()='Callers']"
    sort_by_duration = "//div[text()='Duration']"
    sort_by_recording_options = "//div[text()='Recording Options']"
    sort_by_size = "//div[text()='Size']"

    ### Work with table
    open_recording = "//i[@class='fa fa-plus icon-plus'][1]"
    close_recording = "//i[@class='fa fa-minus icon-minus'][1]"

    download = "//i[@class='fa fa-download fa-lg']"
    play = "//i[@class='fa fa-play fa-lg']"
    trash = "//i[@class='fa fa-trash fa-lg']"

###   Titles   ###
    registration_letter_title = "//span[text()='QA MODE:SimpleTollFree.com Account Registration']"
    login_title = "Account Information - SimpleTollFree"
    account_info = "Account Information - SimpleTollFree"
    recordings = "History & Recordings - SimpleTollFree"
    yandex_page = "https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1"