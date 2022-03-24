import sys

from cx_Freeze import *

includefiles = ['calculator.ico']
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    (
        "DesktopShortcut", #Shortcut
        "DesktopFolder", #Directory_
        "My Calculator", #Name
        "TARGETDIR", #Component_
        "[TARGETDIR]\mycalculator.exe", #Target
        None, #Arguents
        None, #Description
        None, #Hotkey
        None, #Icon
        None, #IconIndex
        None, #ShowCmd
        "TARGETDIR", #wkDir
    )
]
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {"data": msi_data}
setup(
    version = "0.1",
    description = "My Calculator",
    author = "Yash",
    name = "My Calculator",
    options={'build_exe': {'include_files':includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="smartcalculator.py",
            base=base,
            icon="calculator.ico",
        )
    ]
)