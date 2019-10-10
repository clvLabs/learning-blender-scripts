import bpy
import random
from mathutils import Color

# Configuration

# Variables
matlist = []
groundmat = None
matcount = 0

def getrand():
    randmatidx = random.randint(0, matcount-1)
    return matlist[randmatidx]

def setrand(obj):
  obj.active_material = getrand()

def getground():
  return groundmat

def setground(obj):
  obj.active_material = getground()

def init(count):
  global matcount, groundmat
  matcount = count

  for i in range(matcount):
    bpy.ops.material.new()
    new_mat = bpy.data.materials[-1]  # the new material is the last one in the list
    # new_mat.name = f"test_material_{i}"
    new_mat.use_nodes = True

    # ---- Principled BDSF inputs ----- https://blender.stackexchange.com/questions/105463/principled-shader-inputs
    # 0: Base Color
    # 4: Metallic
    # 7: Roughness

    # Base color
    h = random.random()
    s = 1.0
    v = random.random() + 0.2
    a = 1.0

    c = Color()
    c.hsv = h, s, v

    new_mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (c.r, c.g, c.b, a)

    # Metallic
    new_mat.node_tree.nodes["Principled BSDF"].inputs[4].default_value = random.random()

    # Roughness
    new_mat.node_tree.nodes["Principled BSDF"].inputs[7].default_value = random.random()

    matlist.append(new_mat)

  # Ground material
  bpy.ops.material.new()
  groundmat = bpy.data.materials[-1]  # the new material is the last one in the list
  groundmat.name = f"ground"
  groundmat.use_nodes = True

  # Base color
  groundmat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0, 0, 0, 1)

  # Metallic
  groundmat.node_tree.nodes["Principled BSDF"].inputs[4].default_value = 0

  # Roughness
  groundmat.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0.4
