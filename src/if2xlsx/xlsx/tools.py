import os.path


def renamed(filename, new_name=None):
    if new_name is None:
        return filename
    pth = os.path.split(filename)
    dir = list(pth[:-1])
    pnamext = pth[-1]
    _, ext = os.path.splitext(pnamext)
    pth = dir
    pth.append(new_name+ext)
    return os.path.join(*pth)


def name(filename):
    pth = os.path.split(filename)
    pnamext = pth[-1]
    name, ext = os.path.splitext(pnamext)
    return name


def relative_to(filename, obj):
    pfilename = obj.filename
    name = os.path.split(pfilename)[0]
    return os.path.join(name, filename)
