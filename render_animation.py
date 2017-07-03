# This script is an example based on background_job.py, which can be found at
# https://developer.blender.org/diffusion/B/browse/master/release/scripts/templates_py/background_job.py
# This script is to be used with a blender file called rotation_tutorial_2.blend

# This script is an example of how you can run blender from the command line
# (in background mode with no interface) to automate tasks. In this example,
# it renders an animation.
# This example also shows how you can parse command line options to scripts.
#
# Example usage for this test.
#  blender --background rotation_tutorial.blend --python $HOME/render_animation.py -- \
#          --texture="Hello World" \
#          --render="/tmp/hello" \
#          --startframe=1
#		   --endframe=1000
#
# Notice:
# '--' causes blender to ignore all following arguments so python can use them.
#
# See blender --help for details.


import bpy


def render_animation(input_texture_file_name_with_ext, output_video_file_name_without_ext, start_frame, end_frame):
	data = bpy.data
	scene = bpy.context.scene
	
	if input_texture_file_name_with_ext:
		data.images["world"].filepath = "//" + input_texture_file_name_with_ext
	else:
		data.images["world"].filepath = "//world.3x5400x2700_1.jpg"
		
	if output_video_file_name_without_ext:
		scene.render.filepath = "//" + output_video_file_name_without_ext
	else:
		scene.render.filepath = "//Output\\orbit"
		
	if start_frame:
		scene.frame_start = start_frame
	else:
		scene.frame_start = 1
		
	if end_frame:
		scene.frame_end = end_frame
	else:
		scene.frame_end = 1000
		
	bpy.ops.render.render(animation = True, scene = 'Scene')


def is_int(user_input):
	isInt = True
	try:
		val = int(user_input)
	except ValueError:
		isInt = False
	return isInt


def main():
	import sys       # to get command line args
	import argparse  # to parse options for us and print a nice help message

	# get the args passed to blender after "--", all of which are ignored by
	# blender so scripts may receive their own arguments
	argv = sys.argv

	if "--" not in argv:
		argv = []  # as if no args are passed
	else:
		argv = argv[argv.index("--") + 1:]  # get all args after "--"

	# When --help or no args are given, print this help
	usage_text = (
			"Run blender in background mode with this script:"
			"  blender --background --python " + __file__ + " -- [options]"
			)

	parser = argparse.ArgumentParser(description=usage_text)

	# Example utility, add some text and renders or saves it (with options)
	# Possible types are: string, int, long, choice, float and complex.
	parser.add_argument("-t", "--texture", dest = "texture_path", type = str,
		help = "This texture will be wrapped on a 3D model")
	parser.add_argument("-r", "--render", dest = "render_path", type = str,
		help = "Render a video to the specified path")
	parser.add_argument("-sf", "--startframe", dest = "start_frame", type = int,
		help = "Start frame of the animation")
	parser.add_argument("-ef", "--endframe", dest = "end_frame", type = int,
		help = "End frame of the animation")

	args = parser.parse_args(argv)# In this example we wont use the args

	if not argv:
		parser.print_help()
		return

	if args.start_frame and not is_int(args.start_frame):
		print("Error: --startframe=\"some integer\" argument not integer, aborting.")
		parser.print_help()
		return
		
	if args.end_frame and not is_int(args.end_frame):
		print("Error: --endframe=\"some integer\" argument not integer, aborting.")
		parser.print_help()
		return
		
	# Run the example function
	render_animation(args.texture_path, args.render_path, int(args.start_frame), int(args.end_frame))

	print("batch job finished, exiting")
	

if __name__ == "__main__":
	main()
