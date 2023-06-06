import qrcode
# Open file and assign all lines to info(list)
info_file = open('locations.txt', 'r')
info = info_file.readlines()
# convert each link to a QRCode
for i in range(0, len(info), 2):
    img = qrcode.make(info[i])
    img.save(f'images\{info[i + 1][:-1]}.png')
# close file
info_file.close()
