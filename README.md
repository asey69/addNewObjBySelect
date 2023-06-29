# addNewObjBySelect
A tool for maya for creating a new object relative to a selection.

The tool will be useful to anyone who needs to create a new or modify an existing object's hierarchy. The main target audience is riggers, 3D artists.

The tool create new object at the same position of selected object.
The tool alows multiple selection.
The new object will be created and inserted to existing hierarchy.
You can select this position in the hierarchy: before, after or beside the selected object.
Or the new object created outside of the exists hierarchy.
The name of the new object can be changed using user options.
The tool works with reference objects, but in this case the reference hierarchy cannot be changed.

How it works:
Select the needed object or objects in maya scene.
Set optins: 
  What object's type you want to create. Group, locator or joint.
  Use/unuse the namespace.
  How many characters you want to strip from the name of the selected object from the start.
  How many characters you want to strip from the end of the name of the selected object.
Click the appropriate button to create new objects.

Install:
On Windows, scripts are placed under C:\Users\USER_NAME\Documents\maya\#mayaVersion\scripts.
Add to shelf command: AddNewObjBySelectUI()
