import subprocess
import glob, os


def convert_files(filenames):
    if not os.path.exists("textfiles"):
        os.makedirs("textfiles")
    for f in filenames:
        subprocess.run(["pdftotext", f, "textfiles/" + f[:-4] + ".txt"])


if __name__ == "__main__":
    os.chdir("papers")
    filenames = list(glob.glob("*.pdf"))
    convert_files(filenames)
