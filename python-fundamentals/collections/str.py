a_string = "bob"
len(a_string)
print("con" + "cat")
con_cat = "".join(["con", "cat"])
print("a;a;a;".split(";"))

url = "http://www.bob.com"
scheme, _, address = url.partition("://")

"Replace {0} with {1}".format("this", 1)
"With {named} {fields}".format(named="much", fields="better")

import math
print("Math stuff: {math.pi}".format(math=math)) # N.B. Passing objects to format
print("Math stuff: {math.pi:.3F}".format(math=math)) # N.B. Formating
