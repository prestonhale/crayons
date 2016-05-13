

def send_text(voter):
	server = smtplib.SMTP( "smtp.gmail.com", 587 )

	server.starttls()

	server.login( 'crayonsapptest@gmail.com', 'dongdingmountain' )

	chars = '1234567890'
	key = ''.join(random.SystemRandom().choice(chars) for _ in range(5))

	# Send text message through SMS gateway of destination number
	server.sendmail( 'Crayons App', voter.phone+voter.carrier.sms_gateway, key )
	return key