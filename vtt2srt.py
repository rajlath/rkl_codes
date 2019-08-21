import re
import glob, os

reg_m = re.compile(r"(\d{2}):(\d{2}).(\d{3}) --> (\d{2}):(\d{2}).(\d{3})")
reg_h = re.compile(r"(\d{2}):(\d{2}):(\d{2}).(\d{3}) --> (\d{2}):(\d{2}):(\d{2}).(\d{3})")
#00:00.660 --> 00:06.240
# 00:00:00,660 --> 00:00:06,240

def convert_vtt_to_srt(pathname, isdir=False):
    def convert_file(in_file_name):
        out_file_name = pathname[:pathname.rindex(".")]+".srt"
        in_file = open(in_file_name, "r")
        out_file = open(out_file_name, "w")
        indx = 0
        a1, a2 = "00:", "00:"
        for line in in_file.readlines():
            if "WEBVTT" in line:
                continue
            matches = reg_m.match(line)
            if matches:
                a, b, c, d, e, f = matches.groups()
                line = a1 + a +":"+b+","+c+" --> "+a2+d+":"+e+","+f
                indx += 1
                out_file.write(str(indx))
                out_file.write("\n")

            else:
                matches = reg_h.match(line)
                if matches:
                    indx += 1
                    a1, a, b, c, a2, d, e , f = matches.groups()
                    line = a1 + a +":"+b+","+c+" --> "+a2+d+":"+e+","+f
                    out_file.write(str(indx))
                    out_file.write("\n")

            out_file.write(line)
            out_file.write("\n")
        out_file.close()
        in_file.close()

    files = []
    if isdir:
        for file in os.listdir(pathname):
            if file.endswith(".vtt"):
                files.append(os.path.join(pathname, file))
    else:
        files.append(pathname)
    for fname in files:
        convert_file(fname)
        print("{} is converted".format(fname), True)







convert_vtt_to_srt("E:\VideoTutorial\CodingForEnter\SetupYourComputer",True)
