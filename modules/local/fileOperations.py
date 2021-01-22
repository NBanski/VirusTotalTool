import os, mimetypes

# This function scans file and returns path, size in bytes, mimetype/encoding.
def scanFile(path):
    name = path            
    statObject = os.stat(path)
    sizeInbytes = statObject.st_size
    mimetypeEncoding = mimetypes.guess_type(path)
    return(name, sizeInbytes, mimetypeEncoding)

# Returns filename.
def getFileName(path):
    head, tail = os.path.split(path)
    return tail

# Returns filesize in adequate format.
def getFileSize(path):
    statObject = os.stat(path)
    sizeInBytes = statObject.st_size
    sizeInMegabytes = round((sizeInBytes / 1024.0**2), 2)
    sizeInGigabytes = round((sizeInBytes / 1024.0**3), 2)
    if sizeInBytes < 1024:
        return (str(sizeInBytes) + "B")
    elif sizeInBytes > 1024 and sizeInBytes < 1024**3:
        return (str(sizeInMegabytes) + "MB")
    else:
        return (str(sizeInGigabytes) + "GB")

# Returns encoding.
def getFileMimeEncoding(path):
    mimeEncoding = mimetypes.guess_type(path)
    return mimeEncoding