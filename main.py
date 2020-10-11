import subprocess
import datetime
import sys
import os

args = sys.argv
blender = os.environ['blender']
build_script = os.path.join(os.path.dirname(args[0]), 'script.py')
base_directory = os.getcwd()

scene = args[1]
if '-RGB' in args:
    rgb = args[args.index('-RGB') + 1]

t = str(datetime.datetime.now()).replace(':', '.')
time = t[:10] + '_' + t[11:19]
img_name = "img_" + time + ".png"
path_img = os.path.join(base_directory, img_name)
logfile = "log_" + time + ".txt"
path_logfile = os.path.join(base_directory, logfile)

command = [blender, "-b", scene, "-P", build_script, "--", path_img]

if 'rgb' in locals():
    command.append(rgb)

print('Start rendering at ' + time)
with open(path_logfile, 'w') as log:
    process = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log.write(process.stdout)
print('Finished. Created files ' + img_name + ' and ' + logfile)
