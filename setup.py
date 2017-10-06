from cx_Freeze import setup,Executable
setup(name='Face Detector',version='0.1',description='Stuffs',executables=[Executable("faces.py")])