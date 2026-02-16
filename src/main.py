from file_manipulations.copy_static_to_public import *
from file_manipulations.convert_directory import *

COPY_FROM = "static/"
COPY_TO = "public/"
CONTENT = "content"
TEMPLATE = "template.html"

def main():
    shutil.rmtree(COPY_TO)
    copy_static_to_public(COPY_FROM, COPY_TO)
    convert_directory(CONTENT, COPY_TO, TEMPLATE)

if __name__ == "__main__":
    main()