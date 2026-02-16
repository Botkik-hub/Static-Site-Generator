from file_manipulations.copy_static_to_public import *
from file_manipulations.convert_directory import *

import sys

COPY_FROM = "static/"
COPY_TO = "docs/"
CONTENT = "content"
TEMPLATE = "template.html"

def main():
    argv = sys.argv
    if len(argv) < 2:
        basepath = "/"
    else:
        basepath = argv[1]


    copy_from = COPY_FROM #os.path.join(basepath, COPY_FROM)
    copy_to = COPY_TO #os.path.join(basepath, COPY_TO)
    content = CONTENT #os.path.join(basepath, CONTENT)
    template = TEMPLATE #os.path.join(basepath, TEMPLATE)

    print(f"basepath={basepath}, copy_from={copy_from}, copy_to={copy_to}, content={content}, template={template}")
    
    if os.path.exists(copy_to):
        shutil.rmtree(copy_to)  
        
    copy_static_to_public(copy_from, copy_to)
    convert_directory(content, copy_to, template, basepath)

if __name__ == "__main__":
    main()