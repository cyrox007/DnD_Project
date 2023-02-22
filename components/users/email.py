import smtplib as smtp
from email.mime.text import MIMEText
from email.header import Header
import email.message

from settings import config


def email_verification(target, verification_link):
    msg = email.message.Message()
    msg['Subject'] = 'Благодарим вас за регистрацию, пройдите, пожалуйста, проверку почты'
    msg['From'] = config.GMAIL_LOGIN
    msg['To'] = target
    password = config.GMAIL_PASSWORD

    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], password)
    
    email_content = """ <html>
<head>
    <title>Подтвердите ваш адрес электронной почты</title>
    <style type="text/css">
        a {
            text-decoration: none;
            text-align: center;
            color: #fff;
        }
        body,
        #header h1,
        #header h2,
        p {
            margin: 0;
            padding: 0;
        }

        #main {
            border: 1px solid #cfcece;
        }

        img {
            display: block;
        }

        #top-message p,
        #bottom p {
            color: #3f4042;
            font-size: 12px;
            font-family: Arial, Helvetica, sans-serif;
        }

        #header h1 {
            color: #ffffff !important;
            font-family: "Lucida Grande", sans-serif;
            font-size: 24px;
            margin-bottom: 0 !important;
            padding-bottom: 0;
        }

        #header p {
            color: #ffffff !important;
            font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif;
            font-size: 12px;
        }

        h5 {
            margin: 0 0 0.8em 0;
        }

        h5 {
            font-size: 18px;
            color: #444444 !important;
            font-family: Arial, Helvetica, sans-serif;
        }

        p {
            font-size: 12px;
            color: #444444 !important;
            font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4">
        <tr>
            <td>
                <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
                    <tr>
                        <td>
                            <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
                                <tr>
                                    <td width="570" align="center" bgcolor="#d80a3e">
                                        <h1>Благодарим вас за регистрацию в приложении. Подтвердите ваш адрес электронной почты</h1>
                                    </td>
                                </tr>
                                <tr>
                                    <td width="570" align="right" bgcolor="#d80a3e">
                                        
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <table id="content-3" cellpadding="0" cellspacing="0" align="center">
                                <tr>
                                    <td width="250" align="center" valign="top" bgcolor="#d80a3e" style="padding:5px;">
                                        <a href="{0}">Перейтите по ссылке для того чтобы подтвердить регистрацию</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            
                        </td>
                    </tr>
                </table>
                <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
                    <tr>
                        <td align="center">
                            
                        </td>
                    </tr>
                </table><!-- top message -->
            </td>
        </tr>
    </table><!-- wrapper -->
</body>
</html> """.format(verification_link)
    

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print(f"Successfully sent email to {msg['To']}")