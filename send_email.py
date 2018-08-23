import smtplib
from email.mime.text import MIMEText
from email.header import Header

import const
import argparse

parser = argparse.ArgumentParser(description='mailer for notifying finish of command')
parser.add_argument('--title', '-t', default='command finished',
                    help='mail title')
parser.add_argument('--send_to', '-s', default='',
                    help='which address to send')
args = parser.parse_args()
title = args.title
send_to = args.send_to

charset = "iso-2022-jp"
myMailaddress = const.from_email  # 自分のGmailアドレス
password = const.password  # Gmailアカウントのパスワード
toMailaddress = send_to if send_to else const.to_email  # 送信相手のメールアドレス

msg = MIMEText("表題のファイルの実行が完了しました。", "plain", charset)  # メール本文
msg["subject"] = Header(title.encode(charset), charset)  # メールタイトル

# smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)    # Gmailはポート番号587のTLSをサポートしていない！よくわからなければスルーしてね。
smtp_obj = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # Gmailでのメール送信は「smtplib.SMTP_SSL」を用いてポート番号465を使用すること。
smtp_obj.ehlo()  # ehlo()でSMTPサーバーに挨拶しておきましょう。挨拶しておかないとログインできません！
smtp_obj.login(myMailaddress, password)  # ログイン
smtp_obj.sendmail(myMailaddress, toMailaddress, msg.as_string())  # メール送信
smtp_obj.quit()  # ログアウト