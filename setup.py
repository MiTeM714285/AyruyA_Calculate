from cx_Freeze import setup, Executable

buildOptions = {
    "packages": [
        'requests', 'time', 'zipfile', 'shutil', 'os', 'win32gui', 'win32con', 'subprocess'
    ],
    "excludes": [
        "tkinter", "matplotlib"
    ]
}

exe = [Executable('main.py', base='Win32GUI')]

setup(
    name='main',
    version='1.0',
    author='me',
    options=dict(build_exe=buildOptions),
    executables=exe
)