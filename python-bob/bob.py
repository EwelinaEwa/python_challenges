#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what_new = what.strip()
    if what_new == "" or "\t" in what_new:
        return "Fine. Be that way!"
    if what_new[-1] == "!" and what_new[:3] != "Let" or what_new.isupper():
        return "Whoa, chill out!"
    if what_new[-1] == "?":
        return "Sure."

    else:
        return "Whatever."
