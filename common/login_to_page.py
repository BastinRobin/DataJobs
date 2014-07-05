from logging import info, debug
LOGIN_URL = '{base}{login}'

def login(page, host, user, login_params, do_login=True):
    """

    """
    if not do_login:
        info("Not logging into %s", host['base'])
        return False

    url = LOGIN_URL.format(**host)
    info("Logging into %s", url)

    page.open_page(url)
    commands = login_params['commands']

    # select the user
    debug("Setting up user")
    for name, send in user.items():
        this_xpath = login_params[name]
        ele = page.find_xpath(this_xpath)
        page.send(ele, send)

    # Make sure that the send submit and make sure remeber
    # me is selected
    login_commands = login_params['commands']
    if login_commands.has_key('selected'):
        handle_selected_items(page, login_commands['selected'])
    if login_commands.has_key('submitted'):
        handle_submit_items(page, login_commands['submitted'])

    return True

def handle_selected_items(page, selected_items):
    """

    """
    for selected in selected_items:
        ele = page.find_xpath(selected)
        is_selected = ele.is_selected()
        if is_selected: continue
        debug("Clicking: %s", selected)
        ele.click()

def handle_submit_items(page, submitted_items):
    """

    """
    for submit in submitted_items:
        ele = page.find_xpath(submit)
        ele.click()
