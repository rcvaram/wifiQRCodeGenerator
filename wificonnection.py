import qrcode

qr = qrcode.QRCode(version=2,
                   error_correction=qrcode.constants.ERROR_CORRECT_Q,
                   box_size=15,
                   border=5
                   )
#Set your SSID Here

ssid = 'siva'
#Set your password here
password = 'asfsa'
data = 'WIFI:S:<{}>;T:<WPA|WEP|>;P:<{}>;H:<true|false|>;'.format(ssid, password)
qr.add_data(data)
qr.make(fit=True)
img =qr.make_image(fill='black',back_color ='white')
img.save('wifi.png')
