# Making guis

- Following along with [Tech with Time PyQt tutorial](https://www.youtube.com/watch?v=-2uyzAqefyE)

## installation

1. Download Qt python interface: `pip install pyqt5`
2. Download Qt Designer app: `pip install pyqt5-tools`
3. To open designer (it's in your virtual environment folder) `venv_name/Scripts/pyqt5-tools.exe designer`
4. After designing your gui, file -> save as `cytokine_array.ui` (name it whatever you want) and save file in your project folder
5. Export gui to python code: pyuic5 -x cyokine_array.ui -o cytokine_array.py
6. Run gui with: `python cytokine_array.py`

## Bonus: Make it a standalone application with [pyinstaller](https://www.pyinstaller.org/)

1. `pip install pyinstaller`
2. `pyinstaller cytokine_array.py`
   - When complete there will be a new folder called *dist* created
3. in dist find `dist/cytokine_array/cytokine_array.exe` (or similarly named executable) then create a shortcut to and drag that short cut to your desktop (or any where else you like)
