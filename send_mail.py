import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import xlrd, xlwt


def send_email(receiver_email):

    sender = '[Sender Mail Here]'
    receivers = [receiver_email]

    message = MIMEMultipart()
    message['From'] = formataddr(["c7w", sender])
    message['To'] = formataddr([receiver_email.split("@")[0], receivers[0]])

    # Subject
    subject = '【计算机系科协暑培】Linux 账户分发'
    message['Subject'] = Header(subject, 'utf-8')

    # Content
    message.attach(MIMEText('同学你好！现将您的暑培 Linux 账号信息附在附件中，请查收！', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('Account.xls', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="Account.xls"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    att2 = MIMEText(open('Linux.pdf', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="Instruction.pdf"'
    message.attach(att2)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("mails.tsinghua.edu.cn", 25)    # 25 为 SMTP 端口号
        smtpObj.login("[Sender Mail Account Here]", "[Sender Mail Password Here]")
        smtpObj.sendmail(sender, receivers, message.as_string())
        print(f"[Success] {receiver_email}")
    except smtplib.SMTPException as e:
        print(f"[Fail] {receiver_email}")
        print(e)


if __name__ == "__main__":
    sheet = xlrd.open_workbook("账号分配_.xls", formatting_info=True).sheet_by_index(0)

    # import IPython
    # IPython.embed()

    sign_sheet = xlrd.open_workbook("Sign.xlsx").sheet_by_index(0)
    id2mail = {row[1].value.strip(): row[2].value.strip() for row in sign_sheet.get_rows()
               if row[2].value.strip().endswith("@mails.tsinghua.edu.cn")}

    num_rows = sheet.nrows
    for k in range(100, num_rows):
        new_sheet = [sheet.row(0), sheet.row(k)]
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Account')

        try:
            sid = str(int(sheet.row(k)[3].value))
            # Lookup email using sid
            mail = id2mail[sid]

            print(f"[{k}] Processing {sid} {mail}")

        except:
            print(f"[{k}] Continue on {sheet.row(k)[3].value}")
            continue

        for idx, val in enumerate(sheet.row(0)):
            worksheet.write(0, idx, val.value)

        for idx, val in enumerate(sheet.row(k)):
            worksheet.write(1, idx, val.value)

        workbook.save('Account.xls')
        import time
        time.sleep(.5)
        send_email(mail)
