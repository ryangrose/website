
file = open("image_links.txt")

for line in file:
    line = line.rstrip()
    print "<div class=\"col-md-4\">"
    print "\t<div class=\"gallery\">"
    a = "\t\t<a target=\"_blank\" href=\"%s\">"%(line)
    print a
    src = "\t\t\t<img src=\"%s\" alt=\"image\" width=\"600\" height=\"300\">"%(line)
    print src
    print "\t\t</a>"
    print "\t</div>"
    print "</div>"
    print "\n"
