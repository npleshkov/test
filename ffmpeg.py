import os


path_f = []
directory =os.walk('/home/pnm/src/convert/in/')
dir_out = '/home/pnm/src/convert/out/'


#Rename
# for top, dirs, files in directory:
#     for f in files:
# os.rename('a.txt', 'b.kml')

#Decode
for top, dirs, files in directory:
    for f in files:
        path = str(os.path.join(top, f))
        path_out = str(os.path.join(dir_out, str(f)))
        # path_f.append(path)
        print(f' files {path} path_out {path_out}')
        # print(f'{top}  dirs {dirs}  foles {files}  path_f {path}')
        # os.system('ffmpeg -i ' + path + ' -f lavfi -i '
        #                                 'aevalsrc=0 -shortest -c:v libxvid -qscale:v 2 -c:a libmp3lame ' + path_out)
        # #Понижаем громкость звука
        os.system('ffmpeg -i ' + path + ' -f lavfi -i '
                                        'aevalsrc=0 -shortest -c:v libxvid -qscale:v 2 -c:a libmp3lame -af "volume=-7dB" ' + path_out)
        # print(f'{top}  dirs {dirs}  foles {files}  path_f {path}')