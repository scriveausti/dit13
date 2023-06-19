import os
p = os.system("xrandr  | grep \* | cut -d' ' -f4")

print(p)