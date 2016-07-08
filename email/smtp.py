#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def textby(s, textType):
	return MIMEText(s, textType, 'utf-8');

def _format_addr(s):
    name, addr = parseaddr(s);
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr));
# chinese need Header() to analysis

from_addr = 'magce.qin@gmail.com';#raw_input('From: ');
password = 'iloveyou5267501';#raw_input('Password: ');
to_addr = 'magce-lili@qq.com';#raw_input('To: ');
smtp_server = 'smtp.gmail.com';#raw_input('SMTP server: ');
port = 587

# msg = textby('hello,man send by Python...', 'plain');     # by text

# msg = textby('<html><body><h1>Hello</h1>' +
#    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#    '</body></html>', 'html');  # by html

# msg['From'] = _format_addr(u'PythonHbi <%s>' % from_addr);
# msg['To'] = _format_addr(u'lili <%s>' % to_addr);
# msg['Subject'] = Header(u'send by python smtp', 'utf-8').encode();  # by text & html

# send email by MIMEMultipart
from email.mime.multipart import MIMEMultipart;
from email.mime.base import MIMEBase;
import base64;

# msg = MIMEMultipart(); # nomarl
msg = MIMEMultipart('alternative'); # html & plain
msg['From'] = _format_addr(u'magce_qin: <%s>' % from_addr);
msg['To'] = _format_addr(u'magce-lili <%s>' % to_addr);
msg['Subject'] = Header(u'wakakaka', 'utf-8').encode();

msg.attach(MIMEText('hello.if you dvice can\'t read html code, you will see this!', 'plain', 'utf-8'));
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'));

with open('/Users/magce.qin/Documents/fff.jpeg', 'rb') as f:
	mime = MIMEBase('image', 'jpeg', filename = 'fff.jpeg');
	# add head message
	mime.add_header('Content-Disposition', 'attachment', filename = 'fff.jpeg');
	mime.add_header('Content-ID', '<0>');
	mime.add_header('X-Attachment-Id', '0');
	# read file
	mime.set_payload(f.read());
	# base64
	encoders.encode_base64(mime);
	msg.attach(mime);
# by attach 


server = smtplib.SMTP(smtp_server, port);
server.starttls(); # ssl  encrypt
server.set_debuglevel(1);
server.login(from_addr, password);
server.sendmail(from_addr, [to_addr], msg.as_string());
server.quit();


# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage