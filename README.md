# user

What I learned:
We can't directly iterate all of the attributes a class like you
can a dictionary. Using vars(self) creates a dictionary out of the
attributes which can then be iterated. In this case, we can then print
each key/value pair.