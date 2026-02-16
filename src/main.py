from file_manipulations.copy_static_to_public import *
from file_manipulations.generate_page import *

COPY_FROM = "static/"
COPY_TO = "public/"
PAGE = "content/index.md"
TEMPLATE = "template.html"
PAGE_PATH = "public/index.html"

def main():
    copy_static_to_public(COPY_FROM, COPY_TO)
    generate_page(PAGE, TEMPLATE, PAGE_PATH)

if __name__ == "__main__":
    main()