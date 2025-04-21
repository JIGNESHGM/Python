import os,time

source =["C:/Users/jigne/OneDrive/MCA/Company/Python/Problum Solwing/", "C:/Users/jigne/OneDrive/MCA/Company/Python/"]

target_dir = "C:/Users/jigne/OneDrive/MCA/Company/Python/Problum Solwing/backup/"

get = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
 os.mkdir(target_dir) # make directory
 
zip_command = "zip -qr '%s' %s" % (get, ' '.join(source))
