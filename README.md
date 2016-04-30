# autoVenmo

This program will pay someone via Venmo.  You will need to create a file called venmoInfo.py with the following contents:

        # This file contains the venmo information
        my_u = 'you@gmail.com' #your venmo username or email address
        my_p = 'password' #your venmo password
        payee_name = 'someone@gmail.com' # this is the payee's username or email address
        amount = 'XX.XX' #(this is the amount you want to pay, it must be put in as a string)
        description = 'the venmo description you want to attach to the payment'

Because Venmo requires two-step authorization, you will need to be present the first time you sign in using this program
and do the two-step authorization within one minute.  After one minute, the program will save the needed cookies
used in the selenium webdriver.

Currently this program only works on windows.  You will need the SendKeys and selenium library, as well as the
chromedriver found at:
http://chromedriver.storage.googleapis.com/index.html?path=2.21/

In order to get this working on other operating systems, you will need a substitute for the SendKeys library that
currently only works on Windows.