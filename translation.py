class Translation(object):
     START_TEXT = """<b>𝙎𝘾𝙍𝘼𝙋 𝙈𝘼𝙉 is made to Help you To Retrieve APP ID and API Hash Easily and SAFE!
━━━━━━━━━━━━━━━━━━━━━━━━
Please Enter Your Telegram Phone Number With Country Code Format.
Example : +628xxxxxx</b>
"""
     AFTER_RECVD_CODE_TEXT = """<b>No HP Received!
Please send us the code you received from Telegram!</b>

This code is only used for the purpose of getting the APP ID from my.telegram.org
If you don't trust the dev bot, just get the manual.
"""
     BEFORE_SUCC_LOGIN = "<code>Code Received. Scarpping Web Page. . .</code>"
     ERRED_PAGE = """Hadeh Error. Try Manually

How to Manually Retrieve APP ID and API HASH:
1. Go to my.telegram.org/auth
2. Login to your telegram account
3. Click the API Development menu
4. Fill in the data as below:
• App Title : tgbot
• Short Name : tgbot
• URL : (blank)
• Platforms : desktops
5. Done

If Successful Download Manual Please Try Again on this Bot"""
     CANCELLED_MESG = "<b>Bye! Please /start again to repeat</b>"
     IN_VALID_CODE_PVDED = "<b>The OTP code you entered is WRONG</b>"
     IN_VALID_PHNO_PVDED = "<b>The mobile number you entered is WRONG, Please Enter Your Telegram Phone Number With Country Code Format.\nExample: +628xxxxxxxx</b>"
