import steam.webauth as wa

user = wa.WebAuth('username')

# At a console, cli_login can be used to easily perform all login steps
session = user.cli_login('','','','','english')
session.get('https://store.steampowered.com/account/history')

# Or the login steps be implemented for other situation like so
try:
    user.login('password')
except (wa.CaptchaRequired, wa.LoginIncorrect) as exp:
    if isinstance(exp):
        # ask for new password
        print("Failed")
    else:
        password = ""

    if isinstance(exp, wa.CaptchaRequired):
        print(user.captcha_url)
        # ask a human to solve captcha
    else:
        captcha = None

    user.login(password=password, captcha=captcha)
except wa.EmailCodeRequired:
    user.login(email_code='ZXC123')
except wa.TwoFactorCodeRequired:
    user.login(twofactor_code='ZXC123')

user.session.get('https://store.steampowered.com/account/history/')