import bpy
import random

DISPLACEMENT_FACTOR = 5
GROWTH_FACTOR = 1.05

materials = None
utils = None

def init(_materials, _utils):
  global materials, utils
  (materials, utils) = (_materials, _utils)

def create(createmeshfunc, numobjects, location):
  # Create test mesh
  createmeshfunc(location = location)

  utils.set_currobj_physics(10)
  original_mesh = bpy.context.object
  bpy.ops.object.shade_smooth()
  bpy.ops.object.material_slot_add()
  materials.setrand(original_mesh)

  # Configure duplication
  duplicate_params = {
      "linked":False,
      "mode":"TRANSLATION"
  }

  translate_params = {
      "value":(1.0,1.0,1.0)
  }

  # Run the duplication
  utils.activate(original_mesh)
  for i in range(numobjects):
      # Always duplicate original mesh
      # utils.activate(original_mesh)

      # Calculate new scale
      scalefactor = (random.random() * GROWTH_FACTOR) * (i+1)

      # Displacement
      x = (random.random() - 0.5) * DISPLACEMENT_FACTOR
      y = (random.random() - 0.5) * DISPLACEMENT_FACTOR
      z = 2 * scalefactor # (random.random() - 0.5) * DISPLACEMENT_FACTOR
      translate_params["value"] = (x, y, z)

      # Duplication
      bpy.ops.object.duplicate_move(
        OBJECT_OT_duplicate = duplicate_params,
        TRANSFORM_OT_translate = translate_params
      )
      new_object = bpy.context.view_layer.objects.active

      # Physics
      utils.set_currobj_physics(scalefactor * 10)

      # Material
      materials.setrand(new_object)

      # Scale
      # s = (random.random() + 0.1) % 0.7
      # s = 1
      # new_object.scale = (s, s, s)
      new_object.scale = (scalefactor, scalefactor, scalefactor)

      # Leave unselected
      # utils.deactivate(new_object)


  # Re-select original mesh
  utils.activate(original_mesh)

