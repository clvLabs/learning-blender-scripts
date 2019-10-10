import bpy
import os
import sys
import importlib
from pprint import pprint

# ##################################################
# IMPORTANT
#
# Replace this path to something more realistic
#
REPO_PATH = "/home/myself/src/blender/learning-blender-scripts"
# ##################################################

sys.path.append(REPO_PATH + "/test01/src")

# Own libs
_ownlibs = []
import materials
_ownlibs.append(materials)
import utils
_ownlibs.append(utils)
import falling
_ownlibs.append(falling)

# Trick for Blender
for lib in _ownlibs:
  importlib.reload(lib)


# Configuration
NUM_MATERIALS = 50
NUM_OBJECTS = 7
OBJECT_SEPARATION = 15

# Delete existing objects
utils.cleanup()

# Set world config
utils.setworldconfig()

# Create materials
materials.init(NUM_MATERIALS)

# Create base plane
bpy.ops.mesh.primitive_plane_add(size=600, enter_editmode=False, location=(0, 0, -15))
base_plane = bpy.context.object
bpy.ops.transform.rotate(value=-0.35, orient_axis='X', constraint_axis=(True, False, False))
bpy.ops.rigidbody.object_add()
base_plane.rigid_body.type = 'PASSIVE'
bpy.context.object.rigid_body.collision_shape = 'BOX'
materials.setground(base_plane)
utils.deactivate(base_plane)

# Add falling columns
sep = OBJECT_SEPARATION
falling.init(materials, utils)

falling.create(bpy.ops.mesh.primitive_cube_add, NUM_OBJECTS, location=(0, 0, 0))
falling.create(bpy.ops.mesh.primitive_uv_sphere_add, NUM_OBJECTS, location=(sep*-1, 0, 0))
falling.create(bpy.ops.mesh.primitive_monkey_add, NUM_OBJECTS, location=(sep, 0, 0))

falling.create(bpy.ops.mesh.primitive_torus_add, NUM_OBJECTS, location=(0, sep, 0))
falling.create(bpy.ops.mesh.primitive_cone_add, NUM_OBJECTS, location=(sep*-1, sep, 0))
falling.create(bpy.ops.mesh.primitive_cylinder_add, NUM_OBJECTS, location=(sep, sep, 0))
