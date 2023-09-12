import argparse

# - Create parser
myParser = argparse.ArgumentParser()

# - Add arguments
# e.g. python test.py -t "this is random text""
myParser.add_argument("-t",
                      "--text",
                      action="store",
                      required=True,
                      help="Name of network device")

# e.g. python3 test.py --list "item1" "item2" "item3"
myParser.add_argument("-l1",
                      "--list_one",
                      nargs="+",
                      required=True,
                      help="Takes one or more arguments")

# e.g. python3 test.py --list "item1" "item2" "item3"
myParser.add_argument("-l2",
                      "--list_two",
                      nargs="*",
                      required=True,
                      help="Takes zero or more arguments")

# - Execute the parse_args() method
args = myParser.parse_args()

# - Variables
myText = args.text
myList = args.list_one
myList = args.list_two
