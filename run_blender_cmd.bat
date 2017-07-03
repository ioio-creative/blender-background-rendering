echo Start Measure %Time%>>timer.txt
blender --background rotation_tutorial.blend --python render_animation.py -- --texture="world.3x5400x2700_1.jpg" --render="//Output\\orbit" --startframe=1 --endframe=1000
echo Stop Measure %Time%>>timer.txt