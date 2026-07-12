import sys

AVAILABLE_OPTIONS = ['d','o']
ACCEPTED_EXTENSION = '.axil'

def invoke_parameters_parsing():

    file_path = sys.argv[-1]
    doc_file_target = None
    output_file_target = None

    # Check if no arguments are given to the command
    if len(sys.argv)==1:
        __print_help()
        return
    
    # Parse options
    options = sys.argv[1:-1]
    for i in range(len(options)):
        if options[i][0] == '-':
            print(options[i][1:])
            if options[i][1:] in AVAILABLE_OPTIONS:
                if options[i][1:] == 'd':
                    doc_file_target = options[i+1]

                elif options[i][1:] == 'o':
                    output_file_target = options[i+1]
            else:
                print(f"Unknown option: {options[i]}")
                __print_usage()
        else:
            continue
    
    try:
        file = open(file_path, 'r')
    except Exception as e:
        print(f"axil: {e}")

    return file, doc_file_target, output_file_target
        

 
def __print_help():
    print(
        "usage: axilgen [option] [args]\n"
        "Options:\n"
        "\tTBD\n"
        "\n"
        "Arguments:\n"
        "file\t: file containing the definition of the registers module"
    )

def __print_usage():
    print(
      "usage: axilgen [option] [args]\n"  
    )
