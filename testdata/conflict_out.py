# STOPSHIP: Your alias will conflict with the following imports:
#    foo.bar
# Not touching this file.
import foo.bar


def f():
    foo.bar.boring_function()
    foo.bar.interesting_function()