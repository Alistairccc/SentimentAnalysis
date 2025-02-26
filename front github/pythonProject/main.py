import yagmail

# 发件人邮箱账号
sender_email = "2951655816@qq.com"
# 发件人邮箱密码或应用专用密码
sender_password = "czedpwwoogzxdgjj"

recipient_emails = ["2491394084@qq.com"]
subject = "测试的主题"
content = "测试的内容"
for recipient_email in recipient_emails:
    if "@qq.com" in recipient_email:
        yag = yagmail.SMTP(sender_email, sender_password, host='smtp.qq.com', port=465)
    elif "@gmail.com" in recipient_email:
        yag = yagmail.SMTP(sender_email, sender_password, host='smtp.gmail.com', port=465)
    try:
        yag.send(to=recipient_email, subject=subject, contents=content)
        print(f"邮件发送给{recipient_email}成功")
    except Exception as e:
        print(f"邮件发送给{recipient_email}失败:", e)

