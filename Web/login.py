import urllib, urllib2
import cookielib

HEADERS = [
    ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322)'))
]

DEFAULT_COOKIE_FILE = 'login.cookies'

class WebLogin(object):

    def __init__(self, host, user, params, headers=HEADERS, **kw):

        self._user = user
        self._host = host
        self.headers = headers

        # url for website we want to log in to
        self._add_dict(host)

        # create cookie file
        self.cookie_file = DEFAULT_COOKIE_FILE

        # user provided username and password
        self._add_dict(user)
        self.form_params = params
        self._create_user_data()

        # override defaults
        self._add_dict(kw)

        # set up a cookie jar to store cookies
        self._create_cookie_jar()

        # create the opener objects
        self._create_openers()

        # add the headers to mimic a web-browser
        self._add_headers()

    def _create_openers(self):
        """

        """
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )

    def _add_headers(self):
        """

        """
        self.opener.addheaders = self.headers

    def _create_intital_cookie(self):
        """

        """
        response = self.opener.open(self.base_url)
        self.cj.save()
        response = self.login()
        self.login_response = response

    def _add_dict(self, dict):
        """

        """
        for key, val in dict.items():
            setattr(self, key, val)

    def _create_user_data(self):
        """

        """
        data = {}
        for name, element_name in self.form_params.items():
            # collect the params as elementID == user value (like name or password)
            data[element_name] = getattr(self, name)

        # make sure all elements are from user add, such as remember_me.
        for user_key, user_val in self._user.items():
            if data.has_key(user_key): continue
            data[user_key] = user_val
        self.user_data = data

    def _create_cookie_jar(self):
        """ create cookie jar """
        self.cj = cookielib.MozillaCookieJar(self.cookie_file)

    def login_to_base(self):
        """

        """
        resp = self.opener.open(self.base_url)
        self.cj.save()
        response = self.login()

        self.login_response = response
        return self.login_response


    # method to do login
    def login(self):
        login_data = urllib.urlencode(self.user_data)
        login_url = self.base_url + self.login_action
        # then open it
        response = self.opener.open(login_url, login_data)
        self.cj.save()
        return response
