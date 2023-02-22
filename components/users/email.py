import smtplib as smtp
from email.mime.text import MIMEText
from email.header import Header
import email.message

from settings import config


def email_verification(target, verification_link):
    subject = 'Благодарим вас за регистрацию, пройдите, пожалуйста, проверку почты'
    login = config.GMAIL_LOGIN
    password = config.GMAIL_PASSWORD

    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login, password)
    
    email_content = """ <html>
<head>
    <title>Подтвердите ваш адрес электронной почты</title>
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
                                        <a href="{}">Перейтите по ссылке для того чтобы подтвердить регистрацию</a>
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
    

    mime = MIMEText(email_content, 'html', 'utf-8')
    mime['Subject'] = Header(subject, 'utf-8')
    mime.add_header('Content-Type', 'text/html')
    # send the message via the server.
    server.sendmail(login, target, mime.as_string())
    server.quit()
    print(f"Successfully sent email to {target}")