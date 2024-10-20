import math
# Using this for converting file sizes:
# https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


# 8GB or exactly 7.63GB
print(convert_size(8188293120))
