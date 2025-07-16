import time, sys

indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) 

        if indentIncreasing:
            # Increase the number of spaces:
            indent += 1
            if indent == 20:
                # change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()