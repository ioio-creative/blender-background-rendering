# blender-background-rendering
Run Blender with a Python script in the background

- [What you need] (#what-you-need)
- [Command line usage example] (#command-line-usage-examples)
- [Blender file] (#blender-file)
- [Python script] (#python-script)

I tried to run Blender from the command line (in background mode with no interface) to automate tasks. In this example, it renders an animation. I have only tested the usage on Windows, but I suppose it also works on Mac & Linux, as long as one uses the system-specific file separator in the path arguments (e.g. '\' for Windows or '/' for Mac, but don't take it from me :p) in the command line usage and Python script.

***

## What you need:
- Windows requires cmd.exe (Command Prompt) or powershell.exe (PowerShell)
- OSX, GNU/Linux and other Operating Systems require Bash Shell access
- All Operating Systems require Blender 2.7+
- Source Code Editor with Syntax Highlighting to edit the Script

## Command line usage example:
blender --background rotation_tutorial.blend --python render_animation.py -- \
  --texture="world.3x5400x2700_1.jpg"
  --render="//Output\\orbit"
  --startframe=1
  --endframe=1000

Command line arugments:
'rotation_tutorial.blend' is the Blender file, in which the animation is prepared.
'render_animation.py' is the Python script, which initiates the animation rendering.
The rest of the arguments are specific to the animation in 'rotation_tutorial.blend', and will be explained in the 'Blender file' section later.

Notice:
'--' causes blender to ignore all the following arguments so the Python script can use them.

## Blender file:
The animation in 'rotation_tutorial.blend' took inspiration from the Blender Orbit Animation Tutorial.
https://www.youtube.com/watch?v=nmLjYSmaW48
It consists of 4 spheres of various sizes orbiting a centre sphere. The 5 spheres are textured by Earth maps downloaded from NASA websites. https://visibleearth.nasa.gov/view_cat.php?categoryID=1484
The textures of the spheres can be specified dynamically via the 'texture' argument in the command line usage.
The output path of the video rendered is specified by the 'render' argument. In our command line usage example, 'Output' is a directory under the directory of the Blender file, and the output video will have the name of "'orbit' + start_frame + '-' end_frame + file_extension". In the case of 'rotation_tutorial.blend', the output video would be an AVI file.
In a self-explanatory manner, in the command line usage, the 'startframe' and 'endframe' arguments specify the start frame and end frame of the animation to render respectively.

## Python script:
The script 'render_animation.py' took inspriation from 
https://blender.stackexchange.com/questions/6817/how-to-pass-command-line-arguments-to-a-blender-python-script and
https://developer.blender.org/diffusion/B/browse/master/release/scripts/templates_py/background_job.py
It reads in command line arugments in the main() function, which are then passed into the render_animation() function for specifying some animation rendering settings in Blender (see the 'Blender file' section for details).

Lastly, advanced users may want to check out a Python script by Mikeycal Meyers. His script uses multiple CPU cores to speed up rendering of a single animation.
https://www.youtube.com/watch?v=rgwP5L1bICk&t=31s
https://github.com/mikeycal/the-video-editors-render-script-for-blender#configuring-the-script
