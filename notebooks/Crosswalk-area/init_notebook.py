import os, sys
currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass


# projectFolder = 'C:/AV/Carla/CARLA_0.9.13/WindowsNoEditor/PythonAPI/experiments'
projectFolder = 'E:\\AV\\Carla\\CARLA_0.9.13\\WindowsNoEditor\\PythonAPI\\experiments'
# projectFolder = 'C:\\Users\\ryanc\\Documents\\UCSC\\carla-jaywalker-experiments'
sys.path.append(str(projectFolder))
os.chdir(projectFolder)
print( f"current working dir{os.getcwd()}")
