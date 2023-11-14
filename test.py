
def requirements(filename):
    with open(filename,'r') as file:
        lines = file.readlines()
        requirements = [line.replace("\n","").strip() for line in lines if "-e" not in line ]
    return requirements  