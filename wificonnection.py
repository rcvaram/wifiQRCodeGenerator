import optparse

import qrcode


def getArguments():
  parser = optparse.OptionParser()
  parser.add_option("-s", "--ssid", dest="ssid", help="Enter your WIFI SSID")
  parser.add_option("-p", "--password", dest="password",
                    help="Enter your WIFI password")

  args_options, arguments = parser.parse_args()
  return args_options


def createQRCode(ssid, password):
  qr = qrcode.QRCode(version=2,
                     error_correction=qrcode.constants.ERROR_CORRECT_Q,
                     box_size=15,
                     border=5
                     )
  data = 'WIFI:S:<{}>;T:<WPA>;P:<{}>;H:<false>;'.format(ssid, password)
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill='black', back_color='white')
  img.save('wifi.png')


options = getArguments()

if options.ssid is not None:
  if options.password is not None:
    createQRCode(ssid=options.ssid, password=options.password)
    print('Your QR Code is generated successfully for the {} SSID'.format(
      options.ssid))
  else:
    print('Please enter your {} network password'.format(options.ssid))
else:
  print('Please Enter Your SSID First...............')
