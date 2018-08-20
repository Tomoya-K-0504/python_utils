import smtplib
from email.mime.text import MIMEText
from email.header import Header

import const

charset = "iso-2022-jp"
myMailaddress = const.from_email  # 自分のGmailアドレス
password = const.password  # Gmailアカウントのパスワード
toMailaddress = const.to_email  # 送信相手のメールアドレス

msg = MIMEText("ちゃんと送信できていますか？", "plain", charset)  # メール本文
msg["subject"] = Header("メール送信テスト！".encode(charset), charset)  # メールタイトル

# smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)    # Gmailはポート番号587のTLSをサポートしていない！よくわからなければスルーしてね。
smtp_obj = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # Gmailでのメール送信は「smtplib.SMTP_SSL」を用いてポート番号465を使用すること。
smtp_obj.ehlo()  # ehlo()でSMTPサーバーに挨拶しておきましょう。挨拶しておかないとログインできません！
smtp_obj.login(myMailaddress, password)  # ログイン
smtp_obj.sendmail(myMailaddress, toMailaddress, msg.as_string())  # メール送信
smtp_obj.quit()  # ログアウト