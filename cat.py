import os
import time
o=True
while True:
	os.system("cls")
	if o==True:
		print("\n\
\n\
         />_-----_/>\n\
        |    _   _|\n\
       /      _x_/\n\
      /          |\n\
   __/   \\      )\n\
  /  |_   |  |  |\n\
  | (  \\___\\_)_)\n\
  \\_)")
		o=False
	else:
		print(" \n\
          />_____/>\n\
         /       \\\n\
        |    0   0|\n\
       /      _x_/\n\
      /          |\n\
   __/   \\      )\n\
  /  |_   |  |  |\n\
  | (  \\___\\_)_)\n\
  \\_)")
		o=True
	time.sleep(0.5)
input()