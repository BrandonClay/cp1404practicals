import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("Moving {} into folder {}".format(filename, extension))
        os.rename(filename, "{}/{}".format(extension, filename))


main()
