import bpy

def cleanup():
  # bpy.ops.object.select_all(action="SELECT")
  bpy.ops.object.select_by_type(type='MESH')
  bpy.ops.object.delete(use_global=False)

  for material in bpy.data.materials:
      material.user_clear()
      bpy.data.materials.remove(material)


def setworldconfig():
  bpy.data.worlds['World'].use_nodes = True
  bpy.data.worlds['World'].node_tree.nodes['Background'].inputs[0].default_value = (0, 0, 0, 1)
  bpy.data.worlds['World'].node_tree.nodes['Background'].inputs[1].default_value = 0

  bpy.data.worlds['World'].color = (0, 0, 0)

  # https://blender.stackexchange.com/questions/88142/blender-unwanted-bouncy-physics
  bpy.context.scene.rigidbody_world.use_split_impulse = True
  bpy.context.scene.rigidbody_world.steps_per_second = 300


def activate(obj):
  obj.select_set(True)
  bpy.context.view_layer.objects.active = obj


def deactivate(obj):
  obj.select_set(False)


def set_currobj_physics(mass):
  bpy.ops.rigidbody.object_add()
  # bpy.context.object.rigid_body.collision_shape = 'BOX'
  bpy.context.object.rigid_body.mass = mass  # Mass
  bpy.context.object.rigid_body.friction = 0.8 # Friction
  bpy.context.object.rigid_body.restitution = 0.3  # Bounciness
