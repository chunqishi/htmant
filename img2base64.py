################################################################################
# Name     : imgbase64.py                                                      #
# Brief    : python tool to convert current directory iamges into base64 img   #
#            this <img src="data:image/jpeg;base64,------" alt="" /> can be    #
#            directly included in a html file.                                 #
#                                                                              #
# Url      : http://en.wikipedia.org/wiki/Data_URI_scheme#Web_browser_support  #
# Author   : Chunqi SHI <diligence.cs@gmail.com>                               #
# Copyright: &copy 2013 ~ present Chunqi SHI   <diligence.cs@gmail.com>        #
################################################################################

import glob, os
import sys
from subprocess import call

image_data = None

def imagetopy(image, output_file):
    with open(image, 'rb') as fin:
        image_data = fin.read()

    with open(output_file, 'w') as fout:
        fout.write('image_data = '+ repr(image_data))


def pytoimage(pyfile):
    import PIL.Image, cStringIO
    pymodule = __import__(pyfile)
    img = PIL.Image.open(cStringIO.StringIO(pymodule.image_data))
    img.show()


###
##  http://en.wikipedia.org/wiki/Internet_media_type#Type_image
#
__extmap__ = {
'.gif':'image/gif',
'.png':'image/png',
'.jpg':'image/jpeg',
'.svg':'image/svg+xml'
}

def imagetobase64(image, output_file):
    import base64
    (nam,ext) = os.path.splitext(image)
    nam = os.path.basename(image)
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    with open(output_file, 'w') as fout:
        fout.write('<img src="data:'+__extmap__[ext.lower()]+';base64,'+ encoded_string + '" alt="'+ nam +'"/>')


if __name__ == '__main__':
    os.environ["VERSIONER_PYTHON_PREFER_32_BIT"] = "yes"
    if len(sys.argv) == 1:
        call(["python", __file__, "OK"])
    elif sys.argv[1] == "OK":
        types = ("*.gif", "*.png", "*.jpg")
        fimgs = []
        for t in types:
            fimgs.extend(glob.glob(t))
            fimgs.extend(glob.glob(t.upper()))
        print fimgs
        for fimg in fimgs:
            fpy = fimg + ".html"
            if not os.path.exists(fpy):
                imagetobase64(fimg, fpy)
