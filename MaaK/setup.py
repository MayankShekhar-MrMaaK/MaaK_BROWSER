from cx_Freeze import setup,Executable

setup(
    name="MaaK",
    version=0.1,
    description="MaaK_Browser",
    executables=[Executable("maak.py",base="Win32GUI")],
)