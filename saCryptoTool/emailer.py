import subprocess
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time

#emailHour = 11

def checkTime(emailHour):
	now = datetime.datetime.now()
	if now.hour == emailHour:
		return 1
	else:
		return 0


def setEmailTime(time):
	emailHour = time
	print 'Email hour set to: %f' % time

def sendMail(userid, name, email, valueList, prices, db):

	cursor3 = db.cursor()

	now = datetime.datetime.now()
	if now.hour < 12:
		timeofday = 'morning'
	elif now.hour < 18:
		timeofday = 'afternoon'
	else:
		timeofday = 'evening'
	
	datestring = '%d-%d-%d %d:%d:%d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)

	#intro
	intro = 'Good %s %s!\n\n' \
			'This is your daily crypto update!\n' % (timeofday, name)

	#Value list
	total = 0
	val = 'Here are the values of your coins:\n'
	
	for item in valueList:
		if item != 'Total':
			val = val + '%s - Value: R%.2f (Price: R%.2f)\n' % (item, float(valueList[item]), float(prices[item]))

	val = val + '-------------------\nYour total portfolio value is: R%.2f\n' % float(valueList['Total'])

	# Get the last total from sqlite
	cursor3.execute('SELECT total FROM userTotals WHERE userid = :userid ORDER BY date DESC LIMIT 1', {'userid': userid})

	total = cursor3.fetchone()[0]

	cursor3.execute('INSERT INTO userTotals(userid, username, date, total) VALUES(:userid, :username, :date, :total)', {'userid': userid, 'username': name, 'date': datestring, 'total': valueList['Total']})
	db.commit()

	time.sleep(2)

	#Percentage change
	percentageChange = ((float(valueList['Total']) - total)/abs(total))*100
	change = 'Your percentage change since the last update is: %.2f percent.\n\n' % (percentageChange)

	# sentiment
	if percentageChange < -10:
		sentinence = 'Unfortunately, yesterday was not such a great day for your portfolio :(\n'
	elif percentageChange < -1:
		sentinence = 'Yesterday your portfolio devalued slightly.\n'
	elif percentageChange < 1:
		sentinence = 'Yesterday was neutral for your portfolio.\n'
	elif percentageChange <= 10:
		sentinence = 'Yesterday was a good day for your portfolio.\n'
	else:
		sentinence = 'Yesterday your portfolio did great!\n'

	#outro
	outro = '\nKind regards\n\nCryptoApp'

	msg = intro + sentinence + change + val + outro

	cursor3.execute("SELECT email, password FROM appData WHERE id = 1")
	appEmail, appPass = cursor3.fetchone()

	emsg = MIMEMultipart()
	emsg['From'] = appEmail
	emsg['To'] = email #replace with email
	emsg['Subject'] = str(now.year) + '/' + str(now.month) + '/' + str(now.day) + ' - Crypto Update'
	emsg.attach(MIMEText(msg, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(appEmail, appPass)
	text = emsg.as_string()
	server.sendmail(appEmail, email, text)
	server.quit()
	print 'Update email sent to %s.' % (email)
	time.sleep(5)