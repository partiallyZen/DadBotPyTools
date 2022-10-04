import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
import time


# This is your original photo folder
localPath = 'D:/ToSort/jpg'
destinationPath = 'D:/ToSort/jpg/SortedPhoto'
_TAGS_r = dict(((v, k) for k, v in TAGS.items()))
totalFiles = 0
processedPhotos = 0
notPhotos = 0

def processPhoto(photoPath):
    global processedPhotos, notPhotos
    try:
        with Image.open(photoPath) as im:
            exif_data_PIL = im._getexif()
            print(_TAGS_r["DateTimeOriginal"])
            if exif_data_PIL is not None:
                if exif_data_PIL[_TAGS_r["DateTimeOriginal"]] is not None:
                    fileDate = exif_data_PIL[_TAGS_r["DateTimeOriginal"]]
                    if fileDate != '' and len(fileDate) > 10:
                        fileDate = fileDate.replace(":", "")
                        # my destination folders are named as YYYYMM
                        destinationFolder = fileDate[:6]
                        # if destination folder does not exist, create one
                        if not os.path.isdir(os.path.abspath(os.path.join(destinationPath, destinationFolder))):
                            os.mkdir(os.path.abspath(os.path.join(destinationPath, destinationFolder)))
                        # new name of the photo
                        newPhotoName = os.path.abspath(os.path.join(destinationPath, destinationFolder, fileDate + '.' + im.format))
                        # print(newPhotoName)
                        im.close()
                        shutil.move(photoPath, newPhotoName)
                        processedPhotos += 1
                        print("\r%d photos processed, %d not processed" % (processedPhotos, notPhotos), end='')
            else:
                notPhotos += 1
                print("\r%d photos processed, %d not processed" % (processedPhotos, notPhotos), end='')
    except IOError as err:
        notPhotos += 1
        print("\r%d photos processed, %d not processed" % (processedPhotos, notPhotos), end='')
        pass
    except KeyError:
        notPhotos += 1
        pass

def processFolder(folderPath, countOnly):
    global totalFiles
    for file in os.listdir(folderPath):
        # print(file)
        # read all files and folder
        fileNameIn = os.path.abspath(os.path.join(folderPath, file))
        # print(fileNameIn)
        # if this is a folder, read all files inside
        if os.path.isdir(fileNameIn):
            processFolder(fileNameIn, countOnly)
        # if it's file, process it as a photo
        else:
            if countOnly:
                totalFiles +=1
            else:
                processPhoto(fileNameIn)


def main(argv=None):
    tic = time.perf_counter()
    processFolder(localPath, True)
    print("There are total %d files" % totalFiles)
    processFolder(localPath, False)
    print("\nThere are %d photos processed, %d not processed" % (processedPhotos, notPhotos))
    toc = time.perf_counter()
    print(f"Time used: {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()
