from PIL import Image
from os import walk

def pic_webp(picpath):
  imagePath = picpath.split(".png")[0]
  outputPath = imagePath + ".webp"
  im = Image.open(picpath)
  im.save(outputPath)

for (dirpath, dirname, dirfile) in walk("./"):
  for f in dirfile:
    if (f != ".DS_Store"):
      name = ".".join(f.split(".")[:-1])
      ext = f.split(".")[-1]
      if (ext in ["png"] and "%s.webp" % (name) not in dirfile):
        pic_webp("%s%s" % (dirpath, f))