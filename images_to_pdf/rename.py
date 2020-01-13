import os


def defineRule(old, new, rules):
    """
    Define single rule: replace old with new
    and append the rule to rules(list)
    """

    rule = [old, new]
    rules.append(rule)


def addLeadingZero(oldname):
    path, fname = os.path.split(oldname)
    nameNoExt, ext = os.path.splitext(fname)

    newname = '000' + str(nameNoExt)
    newname = newname[-3:]
    
    return os.path.normpath(os.path.join(path, newname+ext))


def BatchChangeFileName(folder, rules):
    """
    Change file names in folder, according to the rule defined
    """

    files = os.listdir(folder)

    for file in files:
        fullOldName = os.path.normpath(os.path.join(folder, file))
        fullNewName = fullOldName
        for rule in rules:
            fullNewName = fullNewName.replace(rule[0], rule[1])

        # only change name when having differences
        if not fullOldName.__eq__(fullNewName):
            os.rename(fullOldName, fullNewName)
            print(fullOldName, 'is changed to', fullNewName)

rules = []
defineRule('topic', '', rules) # replace topic to empty string

BatchChangeFileName(r'C:\FFOutput', rules)

files = os.listdir(r"C:\FFOutput")
for f in files:
    fullOldName = os.path.join("C:/FFOutput", f)
    fullNewName = addLeadingZero(fullOldName)
    print (fullNewName)
    if not fullOldName.__eq__(fullNewName):
        os.rename(fullOldName, fullNewName)
