import os


def main():
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename).replace(".TXT", ".txt").replace(" ", "_")
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    new_name = filename[0]
    for i, j in enumerate(filename[1:], 1):
        if j.isupper():
            try:
                if "_" in filename:
                    pass
                elif filename[i - 1].islower() or filename[i + 1].islower() and filename[i - 1] != '(':
                    new_name += '_'

            except IndexError:
                pass
        new_name += j
    return new_name


main()
