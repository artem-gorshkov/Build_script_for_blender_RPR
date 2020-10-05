import subprocess, datetime, sys

blender = "C:\\Program Files\\Blender Foundation\\Blender 2.90\\blender.exe"
build_script = "C:\\Users\\HP\\Desktop\\blender_script\\script.py"

base_directory = "C:\\Users\\HP\\Desktop\\blender_script\\"
scene = base_directory + "scene_2.blend"

args = sys.argv
if (len(args) > 1):
    scene = args[1]
    if '-d' in args:
        base_directory = args[args.index('-d') + 1]
    if '-RGB' in args:
        rgb = args[args.index('-RGB') + 1]   

t = str(datetime.datetime.now()).replace(':', '.')
time = t[:10] +'_' + t[11:19]
img_name = "img_" + time + ".png"
path_img = base_directory + img_name
logfile = "log_" + time + ".txt"
path_logfile = base_directory + logfile

command = [blender, "-b", scene, "-P", build_script, "--", path_img]

if 'rgb' in locals():
    command.append(rgb)

print('Start rendering at ' + time)
with open(path_logfile, 'w') as log:
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log.write(process.stdout)
print('Finished. Check files ' + img_name + ' and ' + logfile + ' in directory ' + base_directory) 
