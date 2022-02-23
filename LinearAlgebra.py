# Filename:   LinearAlgebra.py
# Author:     Rafel Amer (rafel.amer AT upc.edu)
# Copyright:  Rafel Amer 2020-2022
#
#             This file contains code from the file add_mesh_3d_function_surface.py
#             distributed with Blender
#
# Disclaimer: This code is presented "as is" and it has been written to learn
#             to use the python scripting language and the Blender sofware to
#             use them in the studies of Linear Algebra and Geometry
#
# License:    This software is free software; you can redistribute it and/or
#             modify it under the terms of either:
#
#             1 the GNU Lesser General Public License as published by the Free
#               Software Foundation; either version 3 of the License, or (at your
#               option) any later version.
#
#             or
#
#             2 the GNU General Public License as published by the Free Software
#               Foundation; either version 2 of the License, or (at your option)
#               any later version.
#
#	          See https://www.gnu.org/licenses/
#########################################################################################
import math
import bpy
import bmesh
from bpy_extras import object_utils
from mathutils import Vector, Matrix, Euler, Quaternion

class Color():
	def __init__(self,r,g,b,name):
		self.r = r
		self.g = g
		self.b = b
		self.name = name
#
#
#
class Colors():
	colorsbyname = {
		'Black' : Color(0,0,0,'Black'),
		'GrayObscure' : Color(0.2,0.2,0.2,'GrayObscure'),
		'GrayDark' : Color(0.4,0.4,0.4,'GrayDark'),
		'GrayLight' : Color(0.6,0.6,0.6,'GrayLight'),
		'GrayPale' : Color(0.8,0.8,0.8,'GrayPale'),
		'White' : Color(1,1,1,'White'),
		'Red' : Color(1,0,0,'Red'),
		'RedDarkHard' : Color(0.8,0,0,'RedDarkHard'),
		'RedLightHard' : Color(1,0.2,0.2,'RedLightHard'),
		'RedDarkFaded' : Color(0.6,0,0,'RedDarkFaded'),
		'RedMediumFaded' : Color(0.8,0.2,0.2,'RedMediumFaded'),
		'RedLightFaded' : Color(1,0.4,0.4,'RedLightFaded'),
		'RedObscureDull' : Color(0.4,0,0,'RedObscureDull'),
		'RedDarkDull' : Color(0.6,0.2,0.2,'RedDarkDull'),
		'RedLightDull' : Color(0.8,0.4,0.4,'RedLightDull'),
		'RedPaleDull' : Color(1,0.6,0.6,'RedPaleDull'),
		'RedObscureWeak' : Color(0.2,0,0,'RedObscureWeak'),
		'RedDarkWeak' : Color(0.4,0.2,0.2,'RedDarkWeak'),
		'RedMediumWeak' : Color(0.6,0.4,0.4,'RedMediumWeak'),
		'RedLightWeak' : Color(0.8,0.6,0.6,'RedLightWeak'),
		'RedPaleWeak' : Color(1,0.8,0.8,'RedPaleWeak'),
		'Orange' : Color(1,0.65,0,'Orange'),
		'OrangeRedDark' : Color(0.6,0.2,0,'OrangeRedDark'),
		'OrangeRedMedium' : Color(0.8,0.4,0.2,'OrangeRedMedium'),
		'OrangeRedLight' : Color(1,0.6,0.4,'OrangeRedLight'),
		'OrangeOrangeRed' : Color(1,0.4,0,'OrangeOrangeRed'),
		'RedOrangeDark' : Color(0.8,0.2,0,'RedOrangeDark'),
		'RedOrangeLight' : Color(1,0.4,0.2,'RedOrangeLight'),
		'RedRedOrange' : Color(1,0.2,0,'RedRedOrange'),
		'OrangeDarkHard' : Color(0.8,0.4,0,'OrangeDarkHard'),
		'OrangeLightHard' : Color(1,0.6,0.2,'OrangeLightHard'),
		'OrangeObscureDull' : Color(0.4,0.2,0,'OrangeObscureDull'),
		'OrangeDarkDull' : Color(0.6,0.4,0.2,'OrangeDarkDull'),
		'OrangeLightDull' : Color(0.8,0.6,0.4,'OrangeLightDull'),
		'OrangePaleDull' : Color(1,0.8,0.6,'OrangePaleDull'),
		'OrangeYellowDark' : Color(0.6,0.4,0,'OrangeYellowDark'),
		'OrangeYellowMedium' : Color(0.8,0.6,0.2,'OrangeYellowMedium'),
		'OrangeYellowLight' : Color(1,0.8,0.4,'OrangeYellowLight'),
		'OrangeOrangeYellow' : Color(1,0.6,0,'OrangeOrangeYellow'),
		'YellowOrangeDark' : Color(0.8,0.6,0,'YellowOrangeDark'),
		'YellowOrangeLight' : Color(1,0.8,0.2,'YellowOrangeLight'),
		'YellowYellowOrange' : Color(1,0.8,0,'YellowYellowOrange'),
		'Yellow' : Color(1,1,0,'Yellow'),
		'YellowDarkHard' : Color(0.8,0.8,0,'YellowDarkHard'),
		'YellowLightHard' : Color(1,1,0.2,'YellowLightHard'),
		'YellowDarkFaded' : Color(0.6,0.6,0,'YellowDarkFaded'),
		'YellowMediumFaded' : Color(0.8,0.8,0.2,'YellowMediumFaded'),
		'YellowLightFaded' : Color(1,1,0.4,'YellowLightFaded'),
		'YellowObscureDull' : Color(0.4,0.4,0,'YellowObscureDull'),
		'YellowDarkDull' : Color(0.6,0.6,0.2,'YellowDarkDull'),
		'YellowLightDull' : Color(0.8,0.8,0.4,'YellowLightDull'),
		'YellowPaleDull' : Color(1,1,0.6,'YellowPaleDull'),
		'YellowObscureWeak' : Color(0.2,0.2,0,'YellowObscureWeak'),
		'YellowDarkWeak' : Color(0.4,0.4,0.2,'YellowDarkWeak'),
		'YellowMediumWeak' : Color(0.6,0.6,0.4,'YellowMediumWeak'),
		'YellowLightWeak' : Color(0.8,0.8,0.6,'YellowLightWeak'),
		'YellowPaleWeak' : Color(1,1,0.8,'YellowPaleWeak'),
		'SpringYellowDark' : Color(0.4,0.6,0,'SpringYellowDark'),
		'SpringYellowMedium' : Color(0.6,0.8,0.2,'SpringYellowMedium'),
		'SpringYellowLight' : Color(0.8,1,0.4,'SpringYellowLight'),
		'SpringSpringYellow' : Color(0.6,1,0,'SpringSpringYellow'),
		'YellowSpringDark' : Color(0.6,0.8,0,'YellowSpringDark'),
		'YellowSpringLight' : Color(0.8,1,0.2,'YellowSpringLight'),
		'YellowYellowSpring' : Color(0.8,1,0,'YellowYellowSpring'),
		'SpringDarkHard' : Color(0.4,0.8,0,'SpringDarkHard'),
		'SpringLightHard' : Color(0.6,1,0.2,'SpringLightHard'),
		'SpringObscureDull' : Color(0.2,0.4,0,'SpringObscureDull'),
		'SpringDarkDull' : Color(0.4,0.6,0.2,'SpringDarkDull'),
		'SpringLightDull' : Color(0.6,0.8,0.4,'SpringLightDull'),
		'SpringPaleDull' : Color(0.8,1,0.6,'SpringPaleDull'),
		'SpringGreenDark' : Color(0.2,0.6,0,'SpringGreenDark'),
		'SpringGreenMedium' : Color(0.4,0.8,0.2,'SpringGreenMedium'),
		'SpringGreenLight' : Color(0.6,1,0.4,'SpringGreenLight'),
		'SpringSpringGreen' : Color(0.4,1,0,'SpringSpringGreen'),
		'GreenSpringDark' : Color(0.2,0.8,0,'GreenSpringDark'),
		'GreenSpringLight' : Color(0.4,1,0.2,'GreenSpringLight'),
		'GreenGreenSpring' : Color(0.2,1,0,'GreenGreenSpring'),
		'Green' : Color(0,1,0,'Green'),
		'GreenDarkHard' : Color(0,0.8,0,'GreenDarkHard'),
		'GreenLightHard' : Color(0.2,1,0.2,'GreenLightHard'),
		'GreenDarkFaded' : Color(0,0.6,0,'GreenDarkFaded'),
		'GreenMediumFaded' : Color(0.2,0.8,0.2,'GreenMediumFaded'),
		'GreenLightFaded' : Color(0.4,1,0.4,'GreenLightFaded'),
		'GreenObscureDull' : Color(0,0.4,0,'GreenObscureDull'),
		'GreenDarkDull' : Color(0.2,0.6,0.2,'GreenDarkDull'),
		'GreenLightDull' : Color(0.4,0.8,0.4,'GreenLightDull'),
		'GreenPaleDull' : Color(0.6,1,0.6,'GreenPaleDull'),
		'GreenObscureWeak' : Color(0,0.2,0,'GreenObscureWeak'),
		'GreenDarkWeak' : Color(0.2,0.4,0.2,'GreenDarkWeak'),
		'GreenMediumWeak' : Color(0.4,0.6,0.4,'GreenMediumWeak'),
		'GreenLightWeak' : Color(0.6,0.8,0.6,'GreenLightWeak'),
		'GreenPaleWeak' : Color(0.8,1,0.8,'GreenPaleWeak'),
		'TealGreenDark' : Color(0,0.6,0.2,'TealGreenDark'),
		'TealGreenMedium' : Color(0.2,0.8,0.4,'TealGreenMedium'),
		'TealGreenLight' : Color(0.4,1,0.6,'TealGreenLight'),
		'TealTealGreen' : Color(0,1,0.4,'TealTealGreen'),
		'GreenTealDark' : Color(0,0.8,0.2,'GreenTealDark'),
		'GreenTealLight' : Color(0.2,1,0.4,'GreenTealLight'),
		'GreenGreenTeal' : Color(0,1,0.2,'GreenGreenTeal'),
		'TealDarkHard' : Color(0,0.8,0.4,'TealDarkHard'),
		'TealLightHard' : Color(0.2,1,0.6,'TealLightHard'),
		'TealObscureDull' : Color(0,0.4,0.2,'TealObscureDull'),
		'TealDarkDull' : Color(0.2,0.6,0.4,'TealDarkDull'),
		'TealLightDull' : Color(0.4,0.8,0.6,'TealLightDull'),
		'TealPaleDull' : Color(0.6,1,0.8,'TealPaleDull'),
		'TealCyanDark' : Color(0,0.6,0.4,'TealCyanDark'),
		'TealCyanMedium' : Color(0.2,0.8,0.6,'TealCyanMedium'),
		'TealCyanLight' : Color(0.4,1,0.8,'TealCyanLight'),
		'TealTealCyan' : Color(0,1,0.6,'TealTealCyan'),
		'CyanTealDark' : Color(0,0.8,0.6,'CyanTealDark'),
		'CyanTealLight' : Color(0.2,1,0.8,'CyanTealLight'),
		'CyanCyanTeal' : Color(0,1,0.8,'CyanCyanTeal'),
		'Cyan' : Color(0,1,1,'Cyan'),
		'CyanDarkHard' : Color(0,0.8,0.8,'CyanDarkHard'),
		'CyanLightHard' : Color(0.2,1,1,'CyanLightHard'),
		'CyanDarkFaded' : Color(0,0.6,0.6,'CyanDarkFaded'),
		'CyanMediumFaded' : Color(0.2,0.8,0.8,'CyanMediumFaded'),
		'CyanLightFaded' : Color(0.4,1,1,'CyanLightFaded'),
		'CyanObscureDull' : Color(0,0.4,0.4,'CyanObscureDull'),
		'CyanDarkDull' : Color(0.2,0.6,0.6,'CyanDarkDull'),
		'CyanLightDull' : Color(0.4,0.8,0.8,'CyanLightDull'),
		'CyanPaleDull' : Color(0.6,1,1,'CyanPaleDull'),
		'CyanObscureWeak' : Color(0,0.2,0.2,'CyanObscureWeak'),
		'CyanDarkWeak' : Color(0.2,0.4,0.4,'CyanDarkWeak'),
		'CyanMediumWeak' : Color(0.4,0.6,0.6,'CyanMediumWeak'),
		'CyanLightWeak' : Color(0.6,0.8,0.8,'CyanLightWeak'),
		'CyanPaleWeak' : Color(0.8,1,1,'CyanPaleWeak'),
		'AzureCyanDark' : Color(0,0.4,0.6,'AzureCyanDark'),
		'AzureCyanMedium' : Color(0.2,0.6,0.8,'AzureCyanMedium'),
		'AzureCyanLight' : Color(0.4,0.8,1,'AzureCyanLight'),
		'AzureAzureCyan' : Color(0,0.6,1,'AzureAzureCyan'),
		'CyanAzureDark' : Color(0,0.6,0.8,'CyanAzureDark'),
		'CyanAzureLight' : Color(0.2,0.8,1,'CyanAzureLight'),
		'CyanCyanAzure' : Color(0,0.8,1,'CyanCyanAzure'),
		'AzureDarkHard' : Color(0,0.4,0.8,'AzureDarkHard'),
		'AzureLightHard' : Color(0.2,0.6,1,'AzureLightHard'),
		'AzureObscureDull' : Color(0,0.2,0.4,'AzureObscureDull'),
		'AzureDarkDull' : Color(0.2,0.4,0.6,'AzureDarkDull'),
		'AzureLightDull' : Color(0.4,0.6,0.8,'AzureLightDull'),
		'AzurePaleDull' : Color(0.6,0.8,1,'AzurePaleDull'),
		'AzureBlueDark' : Color(0,0.2,0.6,'AzureBlueDark'),
		'AzureBlueMedium' : Color(0.2,0.4,0.8,'AzureBlueMedium'),
		'AzureBlueLight' : Color(0.4,0.6,1,'AzureBlueLight'),
		'AzureAzureBlue' : Color(0,0.4,1,'AzureAzureBlue'),
		'BlueAzureDark' : Color(0,0.2,0.8,'BlueAzureDark'),
		'BlueAzureLight' : Color(0.2,0.4,1,'BlueAzureLight'),
		'BlueBlueAzure' : Color(0,0.2,1,'BlueBlueAzure'),
		'Blue' : Color(0,0,1,'Blue'),
		'BlueDarkHard' : Color(0,0,0.8,'BlueDarkHard'),
		'BlueLightHard' : Color(0.2,0.2,1,'BlueLightHard'),
		'BlueDarkFaded' : Color(0,0,0.6,'BlueDarkFaded'),
		'BlueMediumFaded' : Color(0.2,0.2,0.8,'BlueMediumFaded'),
		'BlueLightFaded' : Color(0.4,0.4,1,'BlueLightFaded'),
		'BlueObscureDull' : Color(0,0,0.4,'BlueObscureDull'),
		'BlueDarkDull' : Color(0.2,0.2,0.6,'BlueDarkDull'),
		'BlueLightDull' : Color(0.4,0.4,0.8,'BlueLightDull'),
		'BluePaleDull' : Color(0.6,0.6,1,'BluePaleDull'),
		'BlueObscureWeak' : Color(0,0,0.2,'BlueObscureWeak'),
		'BlueDarkWeak' : Color(0.2,0.2,0.4,'BlueDarkWeak'),
		'BlueMediumWeak' : Color(0.4,0.4,0.6,'BlueMediumWeak'),
		'BlueLightWeak' : Color(0.6,0.6,0.8,'BlueLightWeak'),
		'BluePaleWeak' : Color(0.8,0.8,1,'BluePaleWeak'),
		'VioletBlueDark' : Color(0.2,0,0.6,'VioletBlueDark'),
		'VioletBlueMedium' : Color(0.4,0.2,0.8,'VioletBlueMedium'),
		'VioletBlueLight' : Color(0.6,0.4,1,'VioletBlueLight'),
		'VioletVioletBlue' : Color(0.4,0,1,'VioletVioletBlue'),
		'BlueVioletDark' : Color(0.2,0,0.8,'BlueVioletDark'),
		'BlueVioletLight' : Color(0.4,0.2,1,'BlueVioletLight'),
		'BlueBlueViolet' : Color(0.2,0,1,'BlueBlueViolet'),
		'VioletDarkHard' : Color(0.4,0,0.8,'VioletDarkHard'),
		'VioletLightHard' : Color(0.6,0.2,1,'VioletLightHard'),
		'VioletObscureDull' : Color(0.2,0,0.4,'VioletObscureDull'),
		'VioletDarkDull' : Color(0.4,0.2,0.6,'VioletDarkDull'),
		'VioletLightDull' : Color(0.6,0.4,0.8,'VioletLightDull'),
		'VioletPaleDull' : Color(0.8,0.6,1,'VioletPaleDull'),
		'VioletMagentaDark' : Color(0.4,0,0.6,'VioletMagentaDark'),
		'VioletMagentaMedium' : Color(0.6,0.2,0.8,'VioletMagentaMedium'),
		'VioletMagentaLight' : Color(0.8,0.4,1,'VioletMagentaLight'),
		'VioletVioletMagenta' : Color(0.6,0,1,'VioletVioletMagenta'),
		'MagentaVioletDark' : Color(0.6,0,0.8,'MagentaVioletDark'),
		'MagentaVioletLight' : Color(0.8,0.2,1,'MagentaVioletLight'),
		'MagentaMagentaViolet' : Color(0.8,0,1,'MagentaMagentaViolet'),
		'Magenta' : Color(1,0,1,'Magenta'),
		'MagentaDarkHard' : Color(0.8,0,0.8,'MagentaDarkHard'),
		'MagentaLightHard' : Color(1,0.2,1,'MagentaLightHard'),
		'MagentaDarkFaded' : Color(0.6,0,0.6,'MagentaDarkFaded'),
		'MagentaMediumFaded' : Color(0.8,0.2,0.8,'MagentaMediumFaded'),
		'MagentaLightFaded' : Color(1,0.4,1,'MagentaLightFaded'),
		'MagentaObscureDull' : Color(0.4,0,0.4,'MagentaObscureDull'),
		'MagentaDarkDull' : Color(0.6,0.2,0.6,'MagentaDarkDull'),
		'MagentaLightDull' : Color(0.8,0.4,0.8,'MagentaLightDull'),
		'MagentaPaleDull' : Color(1,0.6,1,'MagentaPaleDull'),
		'MagentaObscureWeak' : Color(0.2,0,0.2,'MagentaObscureWeak'),
		'MagentaDarkWeak' : Color(0.4,0.2,0.4,'MagentaDarkWeak'),
		'MagentaMediumWeak' : Color(0.6,0.4,0.6,'MagentaMediumWeak'),
		'MagentaLightWeak' : Color(0.8,0.6,0.8,'MagentaLightWeak'),
		'MagentaPaleWeak' : Color(1,0.8,1,'MagentaPaleWeak'),
		'PinkMagentaDark' : Color(0.6,0,0.4,'PinkMagentaDark'),
		'PinkMagentaMedium' : Color(0.8,0.2,0.6,'PinkMagentaMedium'),
		'PinkMagentaLight' : Color(1,0.4,0.8,'PinkMagentaLight'),
		'PinkPinkMagenta' : Color(1,0,0.6,'PinkPinkMagenta'),
		'MagentaPinkDark' : Color(0.8,0,0.6,'MagentaPinkDark'),
		'MagentaPinkLight' : Color(1,0.2,0.8,'MagentaPinkLight'),
		'MagentaMagentaPink' : Color(1,0,0.8,'MagentaMagentaPink'),
		'PinkDarkHard' : Color(0.8,0,0.4,'PinkDarkHard'),
		'PinkLightHard' : Color(1,0.2,0.6,'PinkLightHard'),
		'PinkObscureDull' : Color(0.4,0,0.2,'PinkObscureDull'),
		'PinkDarkDull' : Color(0.6,0.2,0.4,'PinkDarkDull'),
		'PinkLightDull' : Color(0.8,0.4,0.6,'PinkLightDull'),
		'PinkPaleDull' : Color(1,0.6,0.8,'PinkPaleDull'),
		'PinkRedDark' : Color(0.6,0,0.2,'PinkRedDark'),
		'PinkRedMedium' : Color(0.8,0.2,0.4,'PinkRedMedium'),
		'PinkRedLight' : Color(1,0.4,0.6,'PinkRedLight'),
		'PinkPinkRed' : Color(1,0,0.4,'PinkPinkRed'),
		'RedPinkDark' : Color(0.8,0,0.2,'RedPinkDark'),
		'RedPinkLight' : Color(1,0.2,0.4,'RedPinkLight'),
		'RedRedPink' : Color(1,0,0.2,'RedRedPink')
	}
	#
	#
	#
	@classmethod
	def color(self,name):
		try:
			color = self.colorsbyname[name]
		except:
			return self.colorsbyname["Black"]
		return color
	#
	#
	#
	@classmethod
	def colors(self,names):
		return [self.colorsbyname[x] for x in names]
#
#
#
class Rotation():
	def __init__(self,angle=None,vector=None,quaternion=None,radians=False):
		if angle is not None:
			if not radians:
				angle = math.radians(angle)
			if not isinstance(vector,Vector):
				vector = Vector(vector)
			self.quaternion = Quaternion(vector,angle)
		elif quaternion is not None:
			self.quaternion = quaternion
		else:
			self.quaternion = (1,0,0,0)
	#
	#
	#
	@classmethod
	def from_euler_angles(self,phi,theta,psi,radians=False):
		if not radians:
			phi = math.radians(phi)
			theta = math.radians(theta)
			psi = math.radians(psi)
		r1 = Matrix.Rotation(psi,3,'Z')
		r2 = Matrix.Rotation(theta,3,'X')
		r3 = Matrix.Rotation(phi,3,'Z')
		m = r3 @ r2 @ r1
		q = m.to_quaternion()
		return self(quaternion=q)
	#
	#
	#
	def apply(self,v):
		return self.quaternion @ v
	#
	#
	#
	def to_axis_angle(self,radians=False):
		v, alpha = self.quaternion.to_axis_angle()
		if radians:
			return v, alpha
		return v, 180*alpha/math.pi
#
#
#
class LinearAlgebra():
	def __init__(self):
		self.scene = bpy.context.scene
		self.objects = bpy.data.objects
		self.meshes = bpy.data.meshes
		self.collection = bpy.context.collection
		self.ops = bpy.ops
		self.colors = Colors.colors(["Red","Green","Blue"])
		self.rotation = None
		self.origin = [0,0,0]
		self.base = [[1,0,0],[0,1,0],[0,0,1]]
		self.defaultcolor = None
	#
	#
	#
	def base_cilinder(self):
		bpy.ops.mesh.primitive_cylinder_add(radius=1,depth=1,enter_editmode=False,location=(0, 0, 0))
		bpy.ops.transform.translate(value=(0, 0, 0.5), orient_type='GLOBAL',orient_matrix_type='GLOBAL',
			constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False,
			proportional_edit_falloff='SMOOTH',proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
		bpy.ops.object.shade_smooth()
		bpy.context.object.name = 'Arrow_stem'
	#
	#
	#
	def base_cone(self):
		bpy.ops.mesh.primitive_cone_add(radius1=1.5, radius2=0, depth=2, enter_editmode=False, location=(0, 0, 0))
		bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL',orient_matrix_type='GLOBAL',
			constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False,
			proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
		bpy.ops.object.shade_smooth()
		bpy.context.object.name = 'Arrow_cone'
	#
	#
	#
	def delete_base_cilinder(self):
		bpy.ops.object.select_all(action='DESELECT')
		bpy.data.objects['Arrow_stem'].select_set(True)
		bpy.ops.object.delete()
	#
	#
	#
	def delete_base_cone(self):
		bpy.ops.object.select_all(action='DESELECT')
		bpy.data.objects['Arrow_cone'].select_set(True)
		bpy.ops.object.delete()
	#
	#
	#
	def set_colors(self,names):
		self.colors = Colors.colors(names)
	#
	#
	#
	def set_default_color(self,name):
		self.defaultcolor = name
	#
	#
	#
	def set_rotation(self,angle=None,vector=None,quaternion=None):
		if angle is not None:
			self.rotation = Rotation(angle,vector)
		elif quaternion is not None:
			self.rotation = Rotation(quaternion=quaternion)
		else:
			self.rotation = Rotation(0,[1,0,0])
	#
	#
	#
	def set_origin(self,vector=[0,0,0]):
		if isinstance(vector,Vector):
			v1 = vector.copy()
		else:
			v1 = Vector(vector)
		self.origin = v1
	#
	#
	#
	def reset_origin(self):
		self.origin = Vector([0,0,0])
	#
	#
	#
	def reset_base(self):
		self.base = [[1,0,0],[0,1,0],[0,0,1]]
	#
	#
	#
	def set_base(self,base,orthonormal=False):
		if orthonormal:
			u1 = base[0]
			u2 = base[1]
			if isinstance(u1,Vector):
				v1 = u1
			else:
				v1 = Vector(u1)
			if isinstance(u2,Vector):
				v2 = u2
			else:
				v2 = Vector(u2)
			v2 = v2 - v2.project(v1)
			v1.normalize()
			v2.normalize()
			v3 = v1.cross(v2)
			self.base=[v1,v2,v3]
		else:
			self.base = base
	#
	#
	#
	def add_material(self,obj,material_name,r,g,b,opacity=1.0):
		material = bpy.data.materials.get(material_name)
		if material is None:
			material = bpy.data.materials.new(material_name)
		material.use_nodes = True
		principled_bsdf = material.node_tree.nodes['Principled BSDF']
		if principled_bsdf is not None:
			#for i, o in enumerate(principled_bsdf.inputs):
			#	print(i, o.name)
			principled_bsdf.inputs['Base Color'].default_value = (r, g, b, 0.5)
			principled_bsdf.inputs['IOR'].default_value = 0.0
			principled_bsdf.inputs['Specular'].default_value = 1.0
			principled_bsdf.inputs['Emission'].default_value = (r, g, b, 0.5)
			principled_bsdf.inputs['Emission Strength'].default_value = 0.0
			if opacity < 1.0:
				material.blend_method = 'BLEND'
				principled_bsdf.inputs['Alpha'].default_value = opacity
			else:
				material.blend_method = 'OPAQUE'
				principled_bsdf.inputs['Alpha'].default_value = 1.0
		obj.active_material = material
	#
	#
	#
	def add_ligth(self,location=[0,0,100],energy=3,direction=[0,0,-1]):
		l = bpy.data.lights.new(name="Light", type='SUN')
		l.energy = energy
		l.specular_factor = 4
		obj = self.objects.new(name="Light", object_data=l)
		obj.rotation_mode = 'QUATERNION'
		obj.location = location
		n = Vector(direction)
		mat = Matrix(self.base)
		mat.transpose()
		n = mat @ n
		z = Vector([0,0,-1])
		quaternion = z.rotation_difference(n)
		obj.rotation_quaternion.rotate(quaternion)
		self.collection.objects.link(obj)
	#
	#
	#
	def add_ligths(self,energy=1):
		self.add_ligth()
		self.add_ligth(location=[100,0,0],direction=[-1,0,0],energy=energy)
		self.add_ligth(location=[0,100,0],direction=[0,-1,0],energy=energy)
		self.add_ligth(location=[-100,0,0],direction=[1,0,0],energy=energy)
		self.add_ligth(location=[0,-100,0],direction=[0,1,0],energy=energy)
	#
	#
	#
	def new_components(self,vector=None):
		if vector is None:
			return Vector([0,0,0])
		if isinstance(vector,Vector):
			u = vector
		else:
			u = Vector(vector)
		if self.rotation is not None:
			mat = self.rotation.quaternion.to_matrix()
			mat.invert()
			u = mat @ u
		mat = Matrix(self.base)
		mat.transpose()
		mat.invert()
		u = mat @ u
		return u
	#
	#
	#
	def new_coordinates(self,point=None):
		if point is None:
			return Vector([0,0,0])
		if isinstance(point,Vector):
			u = point
		else:
			u = Vector(point)
		if self.rotation is not None:
			mat = self.rotation.quaternion.to_matrix()
			mat.invert()
			u = mat @ u
		mat = Matrix(self.base)
		mat.transpose()
		mat.invert()
		u = mat @ (u - Vector(self.origin))
		return u
	#
	#
	#
	def set_cursor(self,origin=[0,0,0],direction=[1,0,0],axis='x'):
		axis = axis.lower()
		if axis not in ['x','y','z']:
			return
		eixos = {'x' : Vector([1,0,0]),
				'y' : Vector([0,1,0]),
				'z' : Vector([0,0,1])
		}
		if isinstance(direction,Vector):
			d = direction
		else:
			d = Vector(direction)
		x = eixos[axis]
		quaternion = x.rotation_difference(d)
		self.scene.cursor.location = origin
		self.scene.cursor.rotation_mode = 'QUATERNION'
		self.scene.cursor.rotation_quaternion = quaternion
	#
	#
	#
	def set_cursor_rotation(self,origin=[0,0,0],rotation=Matrix.Identity(3)):
		m = rotation.copy()
		det = m.determinant()
		if abs(- det - 1.0) < 0.1:
			m[2] = - m[2]
		quaternion = m.to_quaternion()
		self.scene.cursor.location = origin
		self.scene.cursor.rotation_mode = 'QUATERNION'
		self.scene.cursor.rotation_quaternion = quaternion.conjugated()

	#
	#
	#
	def draw_base_axis(self,scale=0.05,head_height=0.15,axis=0,name="Axis",positive=True,zaxis=True):
		self.base_cilinder()
		self.base_cone()
		o = Vector([0,0,0])
		op = Vector(self.origin)
		color = 0

		if axis != 0 and axis < 8:
			scale /= 3

		base = self.base
		if not zaxis:
			base = self.base[0:2]
		for vec in base:
			#
			# Draw the seam
			#
			v = Vector(vec)
			t = bpy.data.objects.get("Arrow_stem")
			obj = t.copy()
			obj.name = "Axis%d" % (color + 1)
			obj.data = obj.data.copy()
			obj.location = o
			obj.scale = (scale,scale,(v - o).length - 2 * head_height)
			obj.rotation_mode = 'QUATERNION'
			obj.rotation_quaternion = (v - o).to_track_quat('Z','Y')
			if self.colors is not None and len(self.colors) > color:
				c = self.colors[color]
				self.add_material(obj,c.name,c.r,c.g,c.b)
			if self.rotation is not None:
				obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location = op
			self.scene.collection.objects.link(obj)
			#
			# Draw the arrow
			#
			t = bpy.data.objects.get("Arrow_cone")
			obj2 = t.copy()
			obj2.name = "Arrow"
			obj2.data = obj2.data.copy()
			obj2.location =  v - 2 * head_height * v / v.length
			obj2.scale = (scale + 0.05,scale + 0.05,head_height)
			obj2.rotation_mode = 'QUATERNION'
			obj2.rotation_quaternion = (v - o).to_track_quat('Z','Y')
			if self.colors is not None and len(self.colors) > color:
				c = self.colors[color]
				self.add_material(obj2,c.name,c.r,c.g,c.b)
			if self.rotation is not None:
				obj2.rotation_quaternion.rotate(self.rotation.quaternion)
				obj2.location.rotate(self.rotation.quaternion)
			obj2.location = op + obj2.location
			self.scene.collection.objects.link(obj2)
			#
			# Draw the line
			#
			obj3 = None
			if axis != 0:
				v = axis * Vector(vec)
				t = bpy.data.objects.get("Arrow_stem")
				obj3 = t.copy()
				obj3.name = "Line"
				obj3.data = obj3.data.copy()
				obj3.location = op - v
				obj3.scale = (scale / 2,scale / 2,(2 * v).length)
				obj3.rotation_mode = 'QUATERNION'
				obj3.rotation_quaternion = v.to_track_quat('Z','Y')
				if self.colors is not None and len(self.colors) > color:
					c = self.colors[color]
					self.add_material(obj3,c.name,c.r,c.g,c.b)
				if self.rotation is not None:
					obj3.rotation_quaternion.rotate(self.rotation.quaternion)
				if positive:
					obj3.location = op
				else:
					if self.rotation is not None:
						v.rotate(self.rotation.quaternion)
					obj3.location = op - v
				self.scene.collection.objects.link(obj3)
			#
			# Joint the three objects
			#
			bpy.ops.object.select_all(action='DESELECT')
			bpy.context.view_layer.objects.active = obj
			obj.select_set(True)
			obj2.select_set(True)
			if obj3 is not None:
				obj3.select_set(True)
			bpy.ops.object.join()
			color += 1
		#
		# Join all the axis
		#
		t1 = bpy.data.objects.get("Axis1")
		t1.name = name
		bpy.ops.object.select_all(action='DESELECT')
		bpy.context.view_layer.objects.active = t1
		t1.select_set(True)
		t2 = bpy.data.objects.get("Axis2")
		t2.select_set(True)
		if zaxis:
			t3 = bpy.data.objects.get("Axis3")
			t3.select_set(True)
		bpy.ops.object.join()
		self.delete_base_cilinder()
		self.delete_base_cone()
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return t1
	#
	#
	def draw_vector(self,vector=None,canonica=False,color="Black",scale=0.05,head_height=0.15,axis=0,name="Vector",positive=True):
		if vector is None:
			return
		self.base_cilinder()
		self.base_cone()
		o = Vector([0,0,0])
		op = Vector(self.origin)
		if color is not None:
			color = Colors.color(color)
		if isinstance(vector,Vector):
			vec = vector
		else:
			vec = Vector(vector)
		v = vec
		if not canonica:
			mat = Matrix(self.base)
			mat.transpose()
			v = mat @ vec

		t = bpy.data.objects.get("Arrow_stem")
		obj = t.copy()
		obj.name = name
		obj.data = obj.data.copy()
		obj.location = o
		obj.scale = (scale,scale,(v - o).length - 2 * head_height)
		obj.rotation_mode = 'QUATERNION'
		obj.rotation_quaternion = (v - o).to_track_quat('Z','Y')
		if color is not None:
			self.add_material(obj,color.name,color.r,color.g,color.b)
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
		obj.location = op
		self.scene.collection.objects.link(obj)

		t = bpy.data.objects.get("Arrow_cone")
		obj2 = t.copy()
		obj2.data = obj2.data.copy()
		obj2.name = "Arrow"
		obj2.location =  v - 2 * head_height * v / v.length
		obj2.scale = (scale + 0.05,scale + 0.05,head_height)
		obj2.rotation_mode = 'QUATERNION'
		obj2.rotation_quaternion = (v - o).to_track_quat('Z','Y')
		if color is not None:
			self.add_material(obj2,color.name,color.r,color.g,color.b)
		if self.rotation is not None:
			obj2.rotation_quaternion.rotate(self.rotation.quaternion)
			obj2.location.rotate(self.rotation.quaternion)
		obj2.location = op + obj2.location
		self.scene.collection.objects.link(obj2)

		obj3 = None
		if axis != 0:
			v = axis * v / v.length
			t = bpy.data.objects.get("Arrow_stem")
			obj3 = t.copy()
			obj3.name = "Generated"
			obj3.data = obj3.data.copy()
			obj3.location = op - v
			obj3.scale = (scale / 2,scale / 2,(2 * v).length)
			obj3.rotation_mode = 'QUATERNION'
			obj3.rotation_quaternion = v.to_track_quat('Z','Y')
			if color is not None:
				self.add_material(obj,color.name,color.r,color.g,color.b)
			if self.rotation is not None:
				obj3.rotation_quaternion.rotate(self.rotation.quaternion)
			if positive:
				obj3.location = op
			else:
				obj3.location = op - v
			self.scene.collection.objects.link(obj3)

		bpy.ops.object.select_all(action='DESELECT')
		bpy.context.view_layer.objects.active = obj
		obj.select_set(True)
		obj2.select_set(True)
		if obj3 is not None:
			obj3.select_set(True)
		bpy.ops.object.join()
		bpy.ops.object.shade_smooth()
		bpy.ops.object.select_all(action='DESELECT')
		self.delete_base_cilinder()
		self.delete_base_cone()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def comp_times_vector(self,u,v):
		return Vector([u.x * v.x,u.y * v.y,u.z * v.z])
	#
	#
	#
	def draw_line(self,start=[1,1,1],end=[10,10,10],scale=0.005,name="Line",color="Black"):
		if start is None or end is None:
			return
		self.base_cilinder()
		o = Vector([0,0,0])
		op = Vector(self.origin)
		if isinstance(start,Vector):
			u = start
		else:
			u = Vector(start)
		if isinstance(end,Vector):
			v = end
		else:
			v = Vector(end)
		mat = Matrix(self.base)
		mat.transpose()
		u = mat @ u
		v = mat @ v
		l = (v - u).length
		t = bpy.data.objects.get("Arrow_stem")
		obj = t.copy()
		obj.name = name
		obj.location = u
		obj.scale = (scale / 2,scale / 2,l)
		obj.rotation_mode = 'QUATERNION'
		obj.rotation_quaternion = (v - u).to_track_quat('Z','Y')
		if color is not None:
			c = Colors.color(color)
			self.add_material(obj,c.name,c.r,c.g,c.b)
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		obj.location = obj.location + op
		self.scene.collection.objects.link(obj)
		bpy.ops.object.shade_flat()
		self.delete_base_cilinder()
		bpy.ops.object.select_all(action='DESELECT')
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_components(self,vector=None,color="Cyan",name="Components",scale=0.005):
		if vector is None:
			return
		if isinstance(vector,Vector):
			v = vector
		else:
			v = Vector(vector)
		mat = Matrix(self.base)
		mat.transpose()
		list = [[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]]
		lines = [[0,1],[1,2],[2,3],[0,3],[0,4],[1,5],[2,6],[3,7],[4,5],[5,6],[6,7],[4,7]]
		vecs = [self.comp_times_vector(v,Vector(x)) for x in list]
		count = 0
		for first, last in lines:
			if count == 0:
				this = name
			else:
				this = f"Line{count}"
			count += 1
			self.draw_line(start=vecs[first],end=vecs[last],scale=scale,name=this,color=color)
		t = bpy.data.objects.get(name)
		list = [t]
		for count in range(1,12):
			obj = bpy.data.objects.get(f"Line{count}")
			if obj is not None:
				list.append(obj)
		t = self.join(list)
		bpy.context.view_layer.objects.active = None
		return t
	#
	#
	#
	def draw_vectors(self,vectors=[],canonica=False,color="Black",scale=0.05,head_height=0.2,name="Vectors",axis=0):
		if len(vectors) == 0:
			return
		count = 0
		for v in vectors:
			if count == 0:
				this = name
			else:
				this = f"Vector{count}"
			count += 1
			t = self.draw_vector(v,canonica,color,scale,head_height,axis,this)
		t = bpy.data.objects.get(name)
		list = [t]
		for count in range(1,len(vectors)+1):
			obj = bpy.data.objects.get(f"Vector{count}")
			if obj is not None:
				list.append(obj)
		t = self.join(list)
		return t
	#
	#
	#
	def draw_plane(self,normal=None,base=None,sizex=10,sizey=10,color="AzureBlueDark",name='Plane',opacity=1.0,thickness=0.01):
		if sizex == 0.0:
			return
		bpy.ops.mesh.primitive_plane_add(size=sizex,enter_editmode=True,location=(0, 0, 0))
		bpy.context.object.name = name
		##### bpy.ops.mesh.subdivide(number_cuts=6,quadcorner='INNERVERT')
		bpy.ops.object.mode_set(mode='OBJECT')
		obj = bpy.data.objects.get(name)
		if sizey is not None and sizey != 0.0:
			t = sizey / sizex
			obj.scale = [1,t,1]
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		if normal is not None and base is not None:
			return
		if base is not None:
			if len(base) != 2:
				return
			if isinstance(base[0],Vector):
			 	v1 = base[0]
			else:
				v1 = Vector(base[0])
			if isinstance(base[1],Vector):
			 	v2 = base[1]
			else:
				v2 = Vector(base[1])
			normal = v1.cross(v2)
		if normal is not None and normal != Vector([0,0,0]):
			n = Vector(normal)
			mat = Matrix(self.base)
			mat.transpose()
			n = mat @ n
			z = Vector([0,0,1])
			quaternion = z.rotation_difference(n)
			obj.rotation_quaternion.rotate(quaternion)
			bpy.ops.object.select_all(action='DESELECT')
		obj.location = op
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def simple_curve(self,f=None,tmin=0.0,tmax=1.0,steps=25,name="Simple curve",symmetry=None,draw=False):
		if f is None:
			return None

		delta = (tmax - tmin)/steps
		t = tmin
		bm = bmesh.new()
		verts = []
		verts2 = []

		for k in range(steps + 1):
			p = f(t)
			q = None
			verts.append(bm.verts.new(p))
			if symmetry == 'XY':
				q = (p[0],p[1],-p[2])
			elif symmetry == 'XZ':
				q = (p[0],-p[1],p[2])
			elif symmetry == 'YZ':
				q = (-p[0],p[1],p[2])
			elif symmetry == 'X':
				q = (p[0],-p[1],-p[2])
			elif symmetry == 'Y':
				q = (-p[0],p[1],-p[2])
			elif symmetry == 'Z':
				q = (-p[0],-p[1],p[2])
			elif symmetry == 'O':
				q = (-p[0],-p[1],-p[2])

			if q is not None:
				verts2.append(bm.verts.new(q))
			t += delta
			if t > tmax:
				t = tmax

		for i in range(len(verts) - 1):
			bm.edges.new([verts[i], verts[i+1]])
			if len(verts2) > 0:
				bm.edges.new([verts2[i], verts2[i+1]])

		me = bpy.data.meshes.new('placeholder_mesh')
		obj = bpy.data.objects.new(name,me)
		bm.to_mesh(me)
		bm.free()

		if draw:
			self.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def add_revolution(self,obj,angle=0.0,steps=1,color="AzureBlueDark"):
		m = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		m.levels = 4
		m.subdivision_type = 'SIMPLE'
		m = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
		m.thickness = 0.025
		m.offset = 1.0
		m = obj.modifiers.new(name="Screw", type='SCREW')
		m.angle = angle
		m.steps = steps
		c = Colors.color("AzureBlueDark")
		self.add_material(obj,c.name,c.r,c.g,c.b,1.0)
		bpy.context.scene.collection.objects.link(obj)
	#
	#
	#
	def draw_elliptic_paraboloid(self,a=0.5,xmin=0.0,xmax=3.0,steps=50,scale=[1,1,1],color="AzureBlueDark",name="EllipticParaboloid",opacity=1.0,thickness=0.05):
		obj = self.simple_curve(f=lambda t:(t,0,a*t**2),tmin=xmin,tmax=xmax,steps=steps,name=name)
		modifier = obj.modifiers.new(name="Screw", type='SCREW')
		modifier.angle = 2 * math.pi
		modifier.steps = 64
		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		self.scene.collection.objects.link(obj)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#   z = a * sqrt(x**2 - b)
	#
	def draw_one_sheet_hyperboloid(self,a=2.0,b=2.0,xmin=math.sqrt(2),xmax=5.0,steps=256,scale=[1,1,1],color="AzureBlueDark",name="HyperboloidOneSheet",opacity=1.0,thickness=0.05):
		if xmin < math.sqrt(b):
			xmin = math.sqrt(b)
		delta = (xmax - xmin) / steps
		x = xmax
		bm = bmesh.new()
		verts = []

		for k in range(steps + 1):
			if x < math.sqrt(b):
				x = math.sqrt(b)
			z = - a * math.sqrt(x**2 - b)
			verts.append(bm.verts.new((x,0,z)))
			x -= delta
		x = math.sqrt(b)
		for k in range(steps):
			x += delta
			z = a * math.sqrt(x**2 - b)
			verts.append(bm.verts.new((x,0,z)))

		for i in range(len(verts) - 1):
			bm.edges.new([verts[i], verts[i+1]])

		me = self.meshes.new('placeholder_mesh')
		obj = self.objects.new(name,me)
		bm.to_mesh(me)
		bm.free()
		modifier = obj.modifiers.new(name="Screw", type='SCREW')
		modifier.angle = 2 * math.pi
		modifier.steps = 96
		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		self.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#	z = a * sqrt(x**2+b)
	#
	def draw_two_sheets_hyperboloid(self,a=2.0,b=1.0,xmin=0.0,xmax=5.0,steps=50,scale=[1,1,1],color="AzureBlueDark",name="HyperboloidTwoSheets",opacity=1.0,thickness=0.05):
		delta = (xmax - xmin) / steps
		x = xmax
		bm = bmesh.new()
		verts = []
		count = 2 * steps + 2
		sign = 1
		for k in range(count):
			if k == steps + 1:
				sign = -1
			z = sign * a * math.sqrt(x**2+b)
			verts.append(bm.verts.new((x,0,z)))
			if k == steps and xmin > 0:
				x = xmin
			else:
				x = x - sign * delta
			if k == 0 or k == steps + 1:
				continue
			bm.edges.new([verts[k-1], verts[k]])

		me = self.meshes.new('placeholder_mesh')
		obj = self.objects.new(name,me)
		bm.to_mesh(me)
		bm.free()

		modifier = obj.modifiers.new(name="Screw", type='SCREW')
		modifier.angle = 2 * math.pi
		modifier.steps = 64
		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		self.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#	z = a * x
	#
	def draw_cone(self,a=1.0,xmin=0.0,xmax=5.0,steps=50,scale=[1,1,1],color="AzureBlueDark",name="Cone",opacity=1.0,thickness=0.05):
		delta = (xmax - xmin) / steps
		x = xmax
		bm = bmesh.new()
		verts = []
		count = 2 * steps + 2
		if xmin == 0.0:
			count = 2 * steps + 1
		for k in range(count):
			z = a * x
			verts.append(bm.verts.new((x,0,z)))
			if k == steps and xmin > 0:
				x = - xmin
			else:
				x -= delta
			if k == 0 or (k == steps + 1 and xmin > 0.0):
				continue
			bm.edges.new([verts[k-1], verts[k]])

		me = self.meshes.new('placeholder_mesh')
		obj = self.objects.new(name,me)
		bm.to_mesh(me)
		bm.free()

		modifier = obj.modifiers.new(name="Screw", type='SCREW')
		modifier.angle = 2 * math.pi
		modifier.steps = 64
		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		self.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_parabolic_cylinder(self,p=0.25,xmin=0.0,xmax=6.0,length=20,steps=50,scale=[1,1,1],color="AzureBlueDark",name="ParabolicCylinder",opacity=1.0,thickness=0.05):
		delta = (xmax - xmin) / steps
		x = xmax
		bm = bmesh.new()
		verts = []
		count = 2 * steps + 2
		if xmin == 0.0:
			count = 2 * steps + 1
		for k in range(count):
			z = p * x**2
			verts.append(bm.verts.new((x,0,z)))
			if k == steps and xmin > 0:
				x = - xmin
			else:
				x -= delta
			if k == 0 or (k == steps + 1 and xmin > 0.0):
				continue
			bm.edges.new([verts[k-1], verts[k]])

		me = self.meshes.new('ParabolicCylinderMesh')
		obj = self.objects.new(name, me)
		bm.to_mesh(me)
		bm.free()

		bpy.context.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = obj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_mode(type="EDGE")
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, length, 0),"constraint_axis":(False, True, False),"use_accurate":True})
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode='OBJECT')
		obj.select_set(True)
		bpy.ops.transform.translate(value=(0, -length/2, 0),constraint_axis=(False, True, False))
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
		obj.select_set(False)

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#  z = a * sqrt(x**2 - b)
	#
	def draw_hyperbolic_cylinder(self,a=1.0,b=4.0,xmin=2.0,xmax=6.0,length=20,steps=50,scale=[1,1,1],color="AzureBlueDark",name="HyperbolicCylinder",opacity=1.0,thickness=0.05):
		if xmin < math.sqrt(b):
			xmin = math.sqrt(b)
		delta = (xmax-xmin)/steps
		bm = bmesh.new()
		verts = []
		count = 2 * steps + 2
		if xmin == 0.0:
			count = 2 * steps + 1
		for q, d in [[1,0],[-1,count]]:
			x = xmax
			sign = 1
			for k in range(count):
				if k == steps + 1:
					sign = -1
				if x < math.sqrt(b):
					x = math.sqrt(b)
				y = sign * a * math.sqrt(x**2 - b)
				verts.append(bm.verts.new((q * x,y,0)))
				if k == steps and xmin > math.sqrt(b):
					x = xmin
				else:
					x = x - sign * delta
				if k == 0 or (k == steps + 1 and xmin > 0.0):
					continue
				bm.edges.new([verts[d + k-1], verts[d + k]])

		me = self.meshes.new('HyperboliclinderMesh')
		obj = self.objects.new(name, me)
		bm.to_mesh(me)
		bm.free()

		self.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = obj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_mode(type="EDGE")
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0,0,length),"constraint_axis":(False,False,True),"use_accurate":True})
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode='OBJECT')
		obj.select_set(True)
		bpy.ops.transform.translate(value=(0,0,-length/2),constraint_axis=(False,False,True))
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
		obj.select_set(False)

		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_elliptic_cylinder(self,a=8.0,b=5.0,amin=0.0,amax=2*math.pi,length=20,steps=200,scale=[1,1,1],color="AzureBlueDark",name="EllipticCylinder",opacity=1.0,thickness=0.05):
		if amin < 0.0:
			amin = 0.0
		if amax > 2 * math.pi:
			amax = 2 * math.pi
		delta = (amax-amin)/steps
		bm = bmesh.new()
		verts = []
		t = amin
		for k in range(steps + 1):
			x = a * math.cos(t)
			y = b * math.sin(t)
			verts.append(bm.verts.new((x,y,0)))
			t += delta
			if k == 0:
				continue
			bm.edges.new([verts[k-1], verts[k]])

		me = self.meshes.new('EllipticCylinderMesh')
		obj = self.objects.new(name, me)
		bm.to_mesh(me)
		bm.free()
		self.scene.collection.objects.link(obj)

		bpy.context.view_layer.objects.active = obj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_mode(type="EDGE")
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0,0,length),"constraint_axis":(False,False,True),"use_accurate":True})
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode='OBJECT')
		obj.select_set(True)
		bpy.ops.transform.translate(value=(0,0,-length/2),constraint_axis=(False,False,True))
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
		obj.select_set(False)

		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_hyperbolic_paraboloid(self,a=0.2,b=0.4,xmax=10.0,ymax=10.0,steps=64,scale=[1,1,1],color="AzureBlueDark",name="HyperbolicParaboloid",opacity=1.0,thickness=0.05):
		equation = f"{a} * x**2 - {b} * y**2"
		bpy.ops.mesh.primitive_z_function_surface(equation=equation, div_x=steps, div_y=steps, size_x=xmax, size_y=ymax)
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		obj.select_set(False)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_ellipsoid(self,radius=5.0,scale=[1.2,1.8,0.8],color="AzureBlueDark",name="Ellipsoid",opacity=1.0,thickness=0.05):
		bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=128, radius=radius, enter_editmode=False, location=(0, 0, 0))
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		if self.defaultcolor is not None:
			c = Colors.color(self.defaultcolor)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		obj.location = o
		obj.scale = scale
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.location = op
		bpy.ops.object.shade_smooth()
		obj.select_set(False)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_plane_surface(self,origin=None,normal=None,base=None,sizex=10,sizey=10,vectors=False,scalelines=0.05,scalevector=0.01,
						color="SpringGreenLight",linecolor="GreenDarkDull",vectorcolor="Black",name="Plane",opacity=1.0,thickness=0.0):
		if normal is not None and base is not None:
			return
		if normal is None and base is None:
			return
		mat = Matrix(self.base)
		mat.transpose()
		if normal is not None:
			if not isinstance(normal,Vector):
			 	normal= Vector(normal)
			normal = mat @ normal
		if base is not None:
			if len(base) != 2:
				return
			if isinstance(base[0],Vector):
			 	v1 = base[0]
			else:
				v1 = Vector(base[0])
			if isinstance(base[1],Vector):
			 	v2 = base[1]
			else:
				v2 = Vector(base[1])
			v1 = mat @ v1
			v2 = mat @ v2
			normal = v1.cross(v2)

		if normal == Vector([0,0,0]):
			return

		steps = 4
		delta = sizex / steps
		x = - sizex / 2
		bm = bmesh.new()
		verts = []
		for k in range(steps + 1):
			verts.append(bm.verts.new((x,0,0)))
			x += delta
			if k == 0:
				continue
			bm.edges.new([verts[k-1], verts[k]])

		me = self.meshes.new('PlaneSurfaceMesh')
		obj = self.objects.new('PlaneSurface', me)
		bm.to_mesh(me)
		bm.free()

		bpy.context.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = obj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_mode(type="EDGE")
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, sizey, 0),"constraint_axis":(False, True, False),"use_accurate":True})
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode='OBJECT')
		obj.select_set(True)
		bpy.ops.transform.translate(value=(0, -sizey/2, 0),constraint_axis=(False, True, False))
		bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
		obj.select_set(False)

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		if origin is not None:
			if isinstance(origin,Vector):
				op = op + origin
			else:
				op = op + Vector(origin)
		obj.location = o
		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)

		lines = None
		vecs = None
		s = 0.0
		nodes = [[1,1,0],[-1,1,0],[-1,-1,0],[1,-1,0]]
		nodes = [self.comp_times_vector(Vector([sizex / 2,sizey / 2,0]),Vector(x)) for x in nodes]
		edges = [[0,1],[1,2],[2,3],[3,0]]

		if scalelines > 0.0:
			aux = self.origin
			self.origin = Vector([0,0,0])
			objects = []
			for edge in edges:
				l = self.draw_line(start=nodes[edge[0]],end=nodes[edge[1]],scale=scalelines,name="Lines",color=linecolor)
				objects.append(l)
			lines = self.join(objects)
			self.origin = Vector(aux)
		if lines is not None:
			obj = self.join([obj,lines])

		if vectors:
			vecs = self.draw_vectors(nodes,True,color=vectorcolor,scale=scalevector,head_height=0.2,name="Vectors",axis=0)
		if vecs is not None:
			obj = self.join([obj,vecs])
		obj.name = name

		if isinstance(normal,Vector):
			n = normal
		else:
			n = Vector(normal)
		z = Vector([0,0,1])
		quaternion = z.rotation_difference(n)
		tmp = obj.rotation_quaternion
		quaternion = tmp @ quaternion
		obj.rotation_quaternion = quaternion
		bpy.ops.object.select_all(action='DESELECT')
		obj.location = op
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_point(self,radius=0.01,location=(0,0,0),name="Point",color="AzureBlueDark",opacity=1.0):
		bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=16, radius=radius, enter_editmode=False, location=location)
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)

		if not isinstance(location,Vector):
			location = Vector(location)
		mat = Matrix(self.base)
		mat.transpose()
		location = mat @ location

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		c = Colors.color(color)
		op = Vector(self.origin)
		obj.location = op + location
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		bpy.ops.object.shade_smooth()
		obj.select_set(False)
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_cube(self,origin=None,scale=[1,1,1],scalelines=0.05,vectors=False,color="Blue",linecolor="Red",vectorcolor="Black",name='Cube',opacity=1.0,thickness=0.0):
		bpy.ops.mesh.primitive_cube_add(size=2,enter_editmode=False,align='WORLD',location=(0, 0, 0))
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)
		o = Vector([0,0,0])
		op = Vector(self.origin)
		if origin is not None:
			if isinstance(origin,Vector):
				op = op + origin
			else:
				op = op + Vector(origin)
		obj.location = o
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 0.0

		lines = None
		vecs = None
		s = 0.0
		nodes = [[1+s,1+s,1+s],[-1-s,1+s,1+s],[-1-s,-1-s,1+s],[1+s,-1-s,1+s],
				[1+s,1+s,-1-s],[-1-s,1+s,-1-s],[-1-s,-1-s,-1-s],[1+s,-1-s,-1-s]]
		nodes = [self.comp_times_vector(Vector(scale),Vector(x)) for x in nodes]
		edges =[[0,1],[1,2],[2,3],[3,0],[0,4],[1,5],[2,6],[3,7],[4,5],[5,6],[6,7],[7,4]]
		if scalelines > 0.0:
			objects = []
			for edge in edges:
				l = self.draw_line(start=nodes[edge[0]],end=nodes[edge[1]],scale=scalelines,name="Lines",color=linecolor)
				objects.append(l)
			lines = self.join(objects)

		if vectors:
			vecs = self.draw_vectors(nodes,color=vectorcolor,scale=0.05,head_height=0.2,name="Vectors",axis=0)

		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		obj.scale = scale

		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		obj.location = op
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None
		if lines is not None:
			obj = self.join([obj,lines])

		if vecs is not None:
			obj = self.join([obj,vecs])
		return obj
	#
	#
	#
	def draw_parallelepiped(self,origin=[0,0,0],u1=[1,0,0],u2=[0,1,0],u3=[0,0,1],scalelines=0.025,color="AzureBlueDark",linecolor="OrangeObscureDull",name='Parallelepiped',opacity=1.0,thickness=0.0):
		op = Vector(self.origin)
		if isinstance(origin,Vector):
			op = op + origin
		else:
			op = op + Vector(origin)
		if not isinstance(u1,Vector):
			u1 = Vector(u1)
		if not isinstance(u2,Vector):
			u2 = Vector(u2)
		if not isinstance(u3,Vector):
			u3 = Vector(u3)

		mat = Matrix(self.base)
		mat.transpose()
		u1 = mat @ u1
		u2 = mat @ u2
		u3 = mat @ u3

		bpy.ops.mesh.primitive_cube_add(size=2,enter_editmode=False,align='WORLD',location=(0, 0, 0))
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)

		verts = obj.data.vertices
		verts[0].co = op
		verts[1].co = op + u3
		verts[2].co = op + u2
		verts[3].co = op + u2 + u3
		verts[4].co = op + u1
		verts[5].co = op + u1 + u3
		verts[6].co = op + u1 + u2
		verts[7].co = op + u1 + u2 + u3

		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 0.0

		lines = None
		s = 0.0
		edges =[[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,6],[3,7],[4,5],[4,6],[5,7],[6,7]]
		if scalelines > 0.0:
			objects = []
			for edge in edges:
				l = self.draw_line(start=verts[edge[0]].co,end=verts[edge[1]].co,scale=scalelines,name="Lines",color=linecolor)
				objects.append(l)
			lines = self.join(objects)

		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)

		if lines is not None:
			obj = self.join([obj,lines])

		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None

		return obj
	#
	#
	#
	def draw_tetrahedron(self,origin=[0,0,0],u1=[2,0,0],u2=[2*math.cos(math.pi/3),2*math.sin(math.pi/3),0],u3=[(2+2*math.cos(math.pi/3))/3,2*math.sin(math.pi/3)/3,2],scalelines=0.025,color="AzureBlueDark",linecolor="OrangeObscureDull",name='Tetrahedron',opacity=1.0,thickness=0.0):
		op = Vector(self.origin)
		if isinstance(origin,Vector):
			op = op + origin
		else:
			op = op + Vector(origin)
		if not isinstance(u1,Vector):
			u1 = Vector(u1)
		if not isinstance(u2,Vector):
			u2 = Vector(u2)
		if not isinstance(u3,Vector):
			u3 = Vector(u3)

		mat = Matrix(self.base)
		mat.transpose()
		u1 = mat @ u1
		u2 = mat @ u2
		u3 = mat @ u3

		bpy.ops.mesh.primitive_solid_add()
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)

		verts = obj.data.vertices
		verts[0].co = op + u3
		verts[1].co = op
		verts[2].co = op + u1
		verts[3].co = op + u2

		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 0.0

		lines = None
		s = 0.0
		edges =[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
		if scalelines > 0.0:
			objects = []
			for edge in edges:
				l = self.draw_line(start=verts[edge[0]].co,end=verts[edge[1]].co,scale=scalelines,name="Lines",color=linecolor)
				objects.append(l)
			lines = self.join(objects)

		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)

		if lines is not None:
			obj = self.join([obj,lines])

		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None

		return obj
	#
	#
	#
	def draw_pyramid(self,origin=[0,0,0],u1=[1,0,0],u2=[0,1,0],u3=[0.5,0.5,1],scalelines=0.025,color="AzureBlueDark",linecolor="OrangeObscureDull",name='Pyramid',opacity=1.0,thickness=0.0):
		op = Vector(self.origin)
		if isinstance(origin,Vector):
			op = op + origin
		else:
			op = op + Vector(origin)
		if not isinstance(u1,Vector):
			u1 = Vector(u1)
		if not isinstance(u2,Vector):
			u2 = Vector(u2)
		if not isinstance(u3,Vector):
			u3 = Vector(u3)

		mat = Matrix(self.base)
		mat.transpose()
		u1 = mat @ u1
		u2 = mat @ u2
		u3 = mat @ u3

		bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, enter_editmode=False, align='WORLD',vertices=4)
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)

		verts = obj.data.vertices
		verts[0].co = op
		verts[1].co = op + u1
		verts[2].co = op + u1 + u2
		verts[3].co = op + u2
		verts[4].co = op + u3

		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 0.0

		lines = None
		s = 0.0
		edges =[[0,1],[0,3],[0,4],[1,2],[1,4],[2,3],[2,4],[3,4]]
		if scalelines > 0.0:
			objects = []
			for edge in edges:
				l = self.draw_line(start=verts[edge[0]].co,end=verts[edge[1]].co,scale=scalelines,name="Lines",color=linecolor)
				objects.append(l)
			lines = self.join(objects)

		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)

		if lines is not None:
			obj = self.join([obj,lines])

		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None

		return obj
	#
	#
	#
	def draw_parallelogram(self,origin=[0,0,0],u1=[1,0,0],u2=[0,1,0],scalelines=0.025,color="AzureBlueDark",linecolor="OrangeObscureDull",name='Parallelogram',opacity=1.0,thickness=0.0):
		op = Vector(self.origin)
		if isinstance(origin,Vector):
			op = op + origin
		else:
			op = op + Vector(origin)
		if not isinstance(u1,Vector):
			u1 = Vector(u1)
		if not isinstance(u2,Vector):
			u2 = Vector(u2)

		mat = Matrix(self.base)
		mat.transpose()
		u1 = mat @ u1
		u2 = mat @ u2

		bpy.ops.mesh.primitive_plane_add(size=2,enter_editmode=False,align='WORLD',location=(0, 0, 0))
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)

		verts = obj.data.vertices
		verts[0].co = op
		verts[1].co = op + u1
		verts[2].co = op + u2
		verts[3].co = op + u1 + u2

		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 0.0

		lines = None
		s = 0.0
		edges =[[0,1],[0,2],[1,3],[2,3]]
		if scalelines > 0.0:
			objects = []
			for edge in edges:
				l = self.draw_line(start=verts[edge[0]].co,end=verts[edge[1]].co,scale=scalelines,name="Lines",color=linecolor)
				objects.append(l)
			lines = self.join(objects)

		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)

		if lines is not None:
			obj = self.join([obj,lines])

		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None

		return obj
	#
	#
	#
	def draw_polygon(self,origin=[0,0,0],u1=[1,0,0],u2=[0,1,0],points=[[0,0],[1,0],[0,1]],scalelines=0.075,color="AzureBlueDark",linecolor="OrangeObscureDull",name='Polygon',opacity=1.0,thickness=0.0,vectors=None,scalevectors=0.01):
		if len(points) < 3:
			return
		op = Vector(self.origin)
		if isinstance(origin,Vector):
			op = op + origin
		else:
			op = op + Vector(origin)
		if not isinstance(u1,Vector):
			u1 = Vector(u1)
		if not isinstance(u2,Vector):
			u2 = Vector(u2)
		for i in range(len(points)):
			if not isinstance(points[i],Vector):
				points[i] = Vector(points[i])

		mat = Matrix(self.base)
		mat.transpose()
		u1 = mat @ u1
		u2 = mat @ u2

		bpy.ops.curve.simple(Simple_Type='Polygon',Simple_sides=len(points),align='WORLD',location=(0, 0, 0))
		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)
		bpy.ops.object.mode_set(mode='OBJECT')

		verts = obj.data.splines[0].bezier_points
		for i in range(len(verts)):
			verts[i].co = op + points[i][0] * u1 + points[i][1] * u2

		obj.select_set(True)
		bpy.ops.object.convert(target='MESH')

		if thickness > 0.0:
		 	modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
		 	modifier.thickness = thickness
		 	modifier.offset = 0.0

		ps = [op + points[i][0] * u1 + points[i][1] * u2 for i in range(len(points))]
		lines = None
		if scalelines > 0.0:
			objects = []
			for i in range(len(points)):
				l = self.draw_line(start=ps[i],end=ps[(i + 1) % len(points)],scale=scalelines,name="Lines",color=linecolor)
				objects.append(l)
			lines = self.join(objects)

		if vectors is not None:
			old = self.origin
			self.set_origin(op)
			ps = [points[i][0] * u1 + points[i][1] * u2 for i in range(len(points))]
			vecs = self.draw_vectors(ps,color=vectors,scale=scalevectors)
			self.set_origin(old)

		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)

		if lines is not None:
			obj = self.join([obj,lines])
		if vectors is not None:
			obj = self.join([obj,vecs])

		obj.rotation_mode = 'QUATERNION'
		if self.rotation is not None:
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		bpy.ops.object.shade_smooth()
		bpy.context.view_layer.objects.active = None

		return obj
	#
	#
	#
	def draw_regular_polygon(self,origin=[0,0,0],u1=[1,0,0],u2=[0,1,0],vertexs=5,radius=1,scalelines=0.075,color="AzureBlueDark",linecolor="OrangeObscureDull",name='RegularPolygon',opacity=1.0,thickness=0.0,vectors=None):
		angle = 2*math.pi/vertexs
		points = [[radius*math.cos(i*angle),radius*math.sin(i*angle)] for i in range(vertexs)]
		return self.draw_polygon(origin=origin,u1=u1,u2=u2,points=points,scalelines=scalelines,color=color,linecolor=linecolor,name=name,opacity=opacity,thickness=thickness,vectors=vectors,scalevectors=radius/400)
	#
	#
	#
	def draw_triangle(self,origin=[0,0,0],u1=[1,0,0],u2=[0,1,0],points=[[0,0],[1,0],[0,1]],scalelines=0.075,color="AzureBlueDark",linecolor="OrangeObscureDull",name='Polygon',opacity=1.0,thickness=0.0):
		self.draw_polygon(origin=origin,u1=u1,u2=u2,points=[[0,0],[1,0],[0,1]],scalelines=scalelines,color=color,linecolor=linecolor,name="Triangle",opacity=opacity,thickness=thickness)
	#
	#
	#
	def draw_points(self,points=[],name='Points',color="Blue",opacity=1):
		bm = bmesh.new()
		verts = []
		for p in points:
			verts.append(bm.verts.new(p))

		me = self.meshes.new('PointsMesh')
		obj = self.objects.new(name, me)
		bm.to_mesh(me)
		bm.free()
		self.scene.collection.objects.link(obj)
		return obj
	#
	#
	#
	def draw_mesh(self,mesh=None,name='Mesh',color="Blue",opacity=1):
		bm = bmesh.new()
		verts = []
		for p in mesh.points:
			verts.append(bm.verts.new(p))
		edges = [[0,1],[1,2],[2,3],[3,0]]
		for s in mesh.simplices:
			for e in edges:
				v = Vector(mesh.points[s[e[0]]]) - Vector(mesh.points[s[e[1]]])
				edge = [verts[s[e[0]]],verts[s[e[1]]]]
				try:
					bm.edges.new(edge)
				except:
					pass
		me = self.meshes.new('PointsMesh')
		obj = self.objects.new(name, me)
		bm.to_mesh(me)
		bm.free()
		self.scene.collection.objects.link(obj)
		return obj
	#
	#
	#
	def join(self,list):
		if len(list) <= 1:
			return
		bpy.ops.object.select_all(action='DESELECT')
		bpy.context.view_layer.objects.active = list[0]
		for obj in list:
			obj.select_set(True)
		bpy.ops.object.join()
		bpy.ops.object.select_all(action='DESELECT')
		return list[0]
	#
	#
	#
	def ellipsoid(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,c2=1,principal=True,canonica=True,color="AzureBlueDark",name="Ellipsoid",cmax=15,pmax=15,thickness=0.02):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		c = math.sqrt(c2)
		self.draw_ellipsoid(radius=1,scale=[a,b,c],color=color,name=name,thickness=thickness)
	#
	#
	#
	def sphere(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],r2=1,principal=True,canonica=True,color="AzureBlueDark",name="Sphere",cmax=15,pmax=15,thickness=0.02):
		return self.ellipsoid(o=o,u1=u1,u2=u2,a2=r2,b2=r2,c2=r2,principal=principal,canonica=canonica,color=color,name=name,cmax=cmax,pmax=pmax,thickness=thickness)
	#
	#
	#
	def one_sheet_hyperboloid(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,c2=1,principal=True,canonica=True,color="AzureBlueDark",name="OneSheetHyperboloid",xmax=None,cmax=15,pmax=15,thickness=0.02):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		c = math.sqrt(c2)
		if xmax is None:
			xmax=5.0/a + 2
		xmax /= a
		self.draw_one_sheet_hyperboloid(a=1.0,b=1.0,xmin=1.0,xmax=xmax,scale=[a,b,c],color=color,name=name,thickness=thickness)
	#
	#
	#
	def two_sheets_hyperboloid(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,c2=1,principal=True,canonica=True,color="AzureBlueDark",name="TwoSheetParaboloid",xmax=None,cmax=15,pmax=15,thickness=0.02):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		c = math.sqrt(c2)
		if xmax is None:
			xmax = 5.0/a + 2
		xmax /= a
		self.draw_two_sheets_hyperboloid(a=1.0,b=1.0,xmin=0.0,xmax=xmax,color=color,scale=[a,b,c],name=name,thickness=thickness)
	#
	#
	#
	def cone(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,c2=1,principal=True,canonica=True,color="AzureBlueDark",name="Cone",xmax=None,cmax=15,pmax=15,thickness=0.02,opacity=1.0):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		c = math.sqrt(c2)
		if xmax is None:
			xmax = 10.0/a + 2
		xmax /= a
		self.draw_cone(a=1.0,xmin=0.0,xmax=xmax,steps=50,color=color,scale=[a,b,c],name=name,thickness=thickness,opacity=opacity)
	#
	#
	#
	def hyperbolic_cylinder(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,principal=True,canonica=True,color="AzureBlueDark",name="HyperbolicCylinder",xmax=None,zmax=20,cmax=15,pmax=15,thickness=0.02):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		if xmax is None:
			xmax = 5.0/a + 2
		xmax /= a
		self.draw_hyperbolic_cylinder(a=1.0,b=1.0,xmin=1.0,xmax=xmax,length=zmax,steps=50,color=color,name=name,scale=[a,b,1],thickness=thickness)
	#
	#
	#
	def elliptic_cylinder(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,principal=True,canonica=True,color="AzureBlueDark",name="EllipticCylinder",zmax=20,cmax=15,pmax=15,thickness=0.02):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		self.draw_elliptic_cylinder(a=1.0,b=1.0,length=zmax,color=color,name=name,scale=[a,b,1],thickness=thickness)
	#
	#
	#
	def elliptic_paraboloid(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,principal=True,canonica=True,color="AzureBlueDark",name="EllipticParaboloid",xmax=None,opacity=1.0,cmax=15,pmax=15,thickness=0.02):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		if xmax is None:
			xmax = 10.0/a
		xmax /= a
		self.draw_elliptic_paraboloid(a=1.0,xmin=0.0,xmax=xmax,steps=50,scale=[a,b,1],color=color,name=name,opacity=opacity,thickness=thickness)
	#
	#
	#
	def hyperbolic_paraboloid(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a2=1,b2=1,principal=True,canonica=True,color="AzureBlueDark",name="HyperbolicParaboloid",xmax=None,ymax=None,cmax=15,pmax=15,thickness=0.02):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		a = math.sqrt(a2)
		b = math.sqrt(b2)
		if xmax is None:
			xmax = 10.0/a + 2
		if ymax is None:
			ymax = 10.0/b + 1
		xmax /= a
		ymax /= b
		self.draw_hyperbolic_paraboloid(a=1.0,b=1.0,xmax=xmax,ymax=ymax,color=color,name=name,scale=[a,b,1],thickness=thickness)
	#
	#
	#
	def parabolic_cylinder(self,o=[0,0,0],u1=[1,0,0],u2=[0,1,0],a=1,principal=True,canonica=True,color="AzureBlueDark",name="ParabolicCylinder",xmax=None,ymax=30,cmax=20,pmax=20,thickness=0.02,opacity=1.0):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		u = Quaternion([1,0,0,0])
		orig = [0,0,0]
		if q != u or o != orig:
			if canonica:
				if principal:
					self.colors = Colors.colors(["White","White","White"])
				else:
					self.colors = Colors.colors(["Red","Green","Blue"])
				self.draw_base_axis(axis = cmax,positive=False,name="Referència canònica")
				self.colors = Colors.colors(["Red","Green","Blue"])
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if principal:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència principal")
		coef = 1.0
		if a < 0:
			coef = -1
		if xmax is None:
			xmax = 5.0/a + 1.5
		xmax /= a
		self.draw_parabolic_cylinder(p=coef,xmin=0.0,xmax=xmax,length=ymax,color=color,name=name,scale=[a,1,1],thickness=thickness,opacity=opacity)
	#
	#
	#
	def draw_simple_curve(self,fun,tmin=0.0,tmax=1.0,steps=25,thickness=0.02,color="White",name="Curve"):
		delta = (tmax - tmin) / steps
		t = tmin

		curve = bpy.data.curves.new('myCurve', type='CURVE')
		curve.dimensions = '3D'
		curve.resolution_u = 2

		line = curve.splines.new('POLY')
		line.points.add(steps)

		for i in range(steps+1):
			p = fun(t)
			p.append(1)
			line.points[i].co = p
			t += delta

		obj = bpy.data.objects.new(name, curve)
		curve.bevel_depth = thickness

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,1.0)
		self.scene.collection.objects.link(obj)
		return obj
	#
	#
	#
	def draw_curve(self,fun,tmin=0.0,tmax=1.0,steps=25,thickness=0.01,name="Curve",color="White",axis=False,zaxis=True,o=Vector([0,0,0]),u1=Vector([1,0,0]),u2=Vector([0,1,0])):
		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		qt = mat.to_quaternion()

		delta = (tmax - tmin) / steps
		t = tmin
		bm = bmesh.new()
		verts = []

		pmax = 0
		for k in range(steps + 1):
			p = fun(t)
			m = max(map(abs,p))
			if m > pmax:
				pmax = m
			verts.append(bm.verts.new(p))
			t += delta
			if t > tmax:
				t = tmax

		for i in range(len(verts) - 1):
			bm.edges.new([verts[i], verts[i+1]])

		me = self.meshes.new('placeholder_mesh')
		obj = self.objects.new(name,me)
		bm.to_mesh(me)
		bm.free()

		modifier = obj.modifiers.new(type='SKIN',name = 'skin')
		for v in obj.data.skin_vertices[0].data:
			v.radius = (thickness,thickness)

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,1.0)
		self.set_origin(o)
		self.set_rotation(quaternion=qt)
		if self.rotation is not None:
			obj.rotation_mode = 'QUATERNION'
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		if axis:
			self.draw_base_axis(axis = pmax+3,positive=False,name="Referència escollida",zaxis=zaxis)
		self.scene.collection.objects.link(obj)
		bpy.ops.object.shade_smooth()
		obj.location = o
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def curve(self,fun,tmin=0.0,tmax=1.0,steps=25,thickness=0.01,name="Curve",color="White",axis=False,zaxis=True,o=Vector([0,0,0]),u1=Vector([1,0,0]),u2=Vector([0,1,0]),symmetry=None,canvi=False):
		obj = self.draw_curve(fun,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=name,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)

		if symmetry is None:
			if canvi:
				self.set_origin(o)
				self.set_base([u1,u2],orthonormal=True)
			return obj
		objs = [obj]
		if not isinstance(symmetry,list):
			symmetry = [symmetry]
		for s in symmetry:
			namem = name + s
			if s == 'XY':
				def f(t):
					p = fun(t)
					return (p[0],p[1],-p[2])
				obj2 = self.draw_curve(f,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=namem,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)
				objs.append(obj2)
			if s == 'XZ':
				def f(t):
					p = fun(t)
					return (p[0],-p[1],p[2])
				obj2 = self.draw_curve(f,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=namem,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)
				objs.append(obj2)
			if s == 'YZ':
				def f(t):
					p = fun(t)
					return (-p[0],p[1],p[2])
				obj2 = self.draw_curve(f,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=namem,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)
				objs.append(obj2)
			if s == 'X':
				def f(t):
					p = fun(t)
					return (p[0],-p[1],-p[2])
				obj2 = self.draw_curve(f,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=namem,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)
				objs.append(obj2)
			if s == 'Y':
				def f(t):
					p = fun(t)
					return (-p[0],p[1],-p[2])
				obj2 = self.draw_curve(f,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=namem,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)
				objs.append(obj2)
			if s == 'Z':
				def f(t):
					p = fun(t)
					return (-p[0],-p[1],p[2])
				obj2 = self.draw_curve(f,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=namem,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)
				objs.append(obj2)
			if s == 'O':
				def f(t):
					p = fun(t)
					return (-p[0],-p[1],-p[2])
				obj2 = self.draw_curve(f,tmin=tmin,tmax=tmax,steps=steps,thickness=thickness,name=namem,color=color,axis=axis,zaxis=zaxis,o=o,u1=u1,u2=u2)
				objs.append(obj2)
		if canvi:
			self.set_origin(o)
			self.set_base([u1,u2],orthonormal=True)
		return self.join(objs)
	#
	#
	#
	def draw_circle(self,center=[0,0,0],u1=Vector([1,0,0]),u2=Vector([0,1,0]),axis=False,zaxis=False,radius=1,steps=25,thickness=0.01,name="Circle",color="White",canvi=False):
		if canvi:
			self.set_origin(center)
			self.set_base([u1,u2],orthonormal=True)
		return self.draw_curve(lambda t: (radius*math.cos(t),radius*math.sin(t),0),tmin=0.0,tmax=2*math.pi,axis=axis,zaxis=zaxis,steps=steps,thickness=thickness,name=name,color=color,o=center,u1=u1,u2=u2)
	#
	#
	#
	def draw_ellipse(self,center=[0,0,0],u1=Vector([1,0,0]),u2=Vector([0,1,0]),a=1,b=1,axis=False,zaxis=False,steps=25,thickness=0.01,name="Ellipse",color="White",canvi=False):
		if canvi:
			self.set_origin(center)
			self.set_base([u1,u2],orthonormal=True)
		return self.draw_curve(lambda t: (a*math.cos(t),b*math.sin(t),0),tmin=0.0,tmax=2*math.pi,axis=axis,zaxis=zaxis,steps=steps,thickness=thickness,name=name,color=color,o=center,u1=u1,u2=u2)
	#
	#
	#
	def draw_parabola(self,center=[0,0,0],u1=Vector([1,0,0]),u2=Vector([0,1,0]),a=1,xmax=3.0,axis=False,zaxis=False,steps=25,thickness=0.01,name="Parabola",color="White",canvi=False):
		if canvi:
			self.set_origin(center)
			self.set_base([u1,u2],orthonormal=True)
		return self.draw_curve(lambda t: (t,a*t**2,0),tmin=-xmax,tmax=xmax,axis=axis,zaxis=zaxis,steps=steps,thickness=thickness,name=name,color=color,o=center,u1=u1,u2=u2)
	#
	#
	#
	def draw_hyperbole(self,center=[0,0,0],u1=Vector([1,0,0]),u2=Vector([0,1,0]),a=1,b=1,ymax=3.0,axis=False,zaxis=False,steps=25,thickness=0.01,name="Hyperbole",color="White",canvi=False):
		c1 = self.draw_curve(lambda t: (a*math.sqrt(1+t**2/b**2),t,0),tmin=-ymax,tmax=ymax,axis=axis,zaxis=zaxis,steps=steps,thickness=thickness,name=name,color=color,o=center,u1=u1,u2=u2)
		c2 = self.draw_curve(lambda t: (-a*math.sqrt(1+t**2/b**2),t,0),tmin=-ymax,tmax=ymax,axis=False,zaxis=False,steps=steps,thickness=thickness,name=name,color=color,o=center,u1=u1,u2=u2)
		self.join([c1,c2])
		if canvi:
			self.set_origin(center)
			self.set_base([u1,u2],orthonormal=True)
		return c1
	#
	#
	#
	def create_mesh_object(self,context,verts,edges,faces,name):
		mesh = bpy.data.meshes.new(name)
		mesh.from_pydata(verts, edges, faces)
		mesh.update()
		return object_utils.object_data_add(context, mesh, operator=None)
	#
	#
	#
	def createFaces(self,vertIdx1,vertIdx2,closed=False,flipped=False):
		faces = []
		if not vertIdx1 or not vertIdx2:
			return None
		if len(vertIdx1) < 2 and len(vertIdx2) < 2:
			return None

		fan = False
		if (len(vertIdx1) != len(vertIdx2)):
			if (len(vertIdx1) == 1 and len(vertIdx2) > 1):
				fan = True
			else:
				return None

		total = len(vertIdx2)
		if closed:
			if flipped:
				face = [vertIdx1[0],vertIdx2[0],vertIdx2[total - 1]]
				if not fan:
					face.append(vertIdx1[total - 1])
				faces.append(face)
			else:
				face = [vertIdx2[0], vertIdx1[0]]
				if not fan:
					face.append(vertIdx1[total - 1])
				face.append(vertIdx2[total - 1])
				faces.append(face)
		for num in range(total - 1):
			if flipped:
				if fan:
					face = [vertIdx2[num], vertIdx1[0], vertIdx2[num + 1]]
				else:
					face = [vertIdx2[num], vertIdx1[num],vertIdx1[num + 1], vertIdx2[num + 1]]
				faces.append(face)
			else:
				if fan:
					face = [vertIdx1[0], vertIdx2[num], vertIdx2[num + 1]]
				else:
					face = [vertIdx1[num], vertIdx2[num],vertIdx2[num + 1], vertIdx1[num + 1]]
				faces.append(face)
		return faces
	#
	#
	#
	def draw_parametric_surface(self,eq,range_u_min,range_u_max,range_u_step,range_v_min,range_v_max,range_v_step,name,wrap_u=False,wrap_v=False,close_v=False):
		verts = []
		faces = []
		if not callable(range_u_min) and not callable(range_u_max):
			uStep = (range_u_max - range_u_min) / range_u_step
		vStep = (range_v_max - range_v_min) / range_v_step
		uRange = range_u_step + 1
		vRange = range_v_step + 1

		if wrap_u:
			uRange = uRange - 1
		if wrap_v:
			vRange = vRange - 1

		for vN in range(vRange):
			v = range_v_min + (vN * vStep)
			print(v)
			if callable(range_u_min):
				u_min = range_u_min(v)
			else:
				u_min = range_u_min
			if callable(range_u_max):
				u_max = range_u_max(v)
			else:
				u_max = range_u_max
			uStep = (u_max - u_min) / range_u_step
			for uN in range(uRange):
				u = u_min + (uN * uStep)
				verts.append(eq(u,v))

		for vN in range(range_v_step):
			vNext = vN + 1
			if vNext >= vRange:
				vNext = 0
			for uN in range(range_u_step):
				uNext = uN + 1
				if uNext >= uRange:
					uNext = 0
				faces.append([(vNext * uRange) + uNext,(vNext * uRange) + uN,(vN * uRange) + uN,(vN * uRange) + uNext])

		if close_v and wrap_u and (not wrap_v):
			for uN in range(1, range_u_step - 1):
				faces.append([range_u_step - 1,range_u_step - 1 - uN,range_u_step - 2 - uN])
				faces.append([range_v_step * uRange,range_v_step * uRange + uN,range_v_step * uRange + uN + 1])
		self.create_mesh_object(bpy.context,verts, [], faces, name)
	#
	#
	#
	def draw_surface(self,eq=None,umin=-1,umax=1,usteps=64,vmin=-1,vmax=1,vsteps=64,thickness=0.02,opacity=1.0,pmax=10,name="Surface",color="AzureBlueDark",axis=False,o=Vector([0,0,0]),u1=Vector([1,0,0]),u2=Vector([0,1,0]),wrap_u=False,wrap_v=False,close_v=False):
		if eq is None:
			return

		if isinstance(u1,Vector):
			v1 = u1
		else:
			v1 = Vector(u1)
		if isinstance(u2,Vector):
			v2 = u2
		else:
			v2 = Vector(u2)
		v2 = v2 - v2.project(v1)
		v1.normalize()
		v2.normalize()
		v3 = v1.cross(v2)
		mat = Matrix([v1,v2,v3])
		mat.transpose()
		q = mat.to_quaternion()
		self.draw_parametric_surface(eq=eq,range_u_min=umin,range_u_max=umax,range_u_step=usteps,range_v_min=vmin,range_v_max=vmax,range_v_step=vsteps,name=name,wrap_u=wrap_u,wrap_v=wrap_v,close_v=close_v)

		bpy.context.object.name = name
		obj = bpy.data.objects.get(name)
		obj.show_wire = False

		modifier = obj.modifiers.new(name="SubSurf", type='SUBSURF')
		modifier.levels = 4
		modifier.subdivision_type = 'SIMPLE'
		if thickness > 0.0:
			modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
			modifier.thickness = thickness
			modifier.offset = 1.0
		c = Colors.color(color)
		self.add_material(obj,c.name,c.r,c.g,c.b,opacity)
		self.set_origin(o)
		self.set_rotation(quaternion=q)
		if self.rotation is not None:
			obj.rotation_mode = 'QUATERNION'
			obj.rotation_quaternion.rotate(self.rotation.quaternion)
			obj.location.rotate(self.rotation.quaternion)
		if axis:
			self.draw_base_axis(axis = pmax,positive=False,name="Referència escollida")

		bpy.ops.object.shade_smooth()
		obj.location = o
		obj.select_set(False)
		bpy.context.view_layer.objects.active = None
		return obj
	#
	#
	#
	def draw_function(self,f=None,xmin=-3,xmax=3,xsteps=64,ymin=-3,ymax=3,ysteps=64,thickness=0.02,opacity=1.0,pmax=10,name="Function",color="AzureBlueDark",axis=False,o=Vector([0,0,0]),u1=Vector([1,0,0]),u2=Vector([0,1,0])):
		return self.draw_surface(eq=lambda x,y:(x,y,f(x,y)),umin=xmin,umax=xmax,usteps=xsteps,vmin=ymin,vmax=ymax,vsteps=ysteps,thickness=thickness,opacity=opacity,pmax=pmax,name=name,color=color,axis=axis,o=o,u1=u1,u2=u2,wrap_u=False,wrap_v=False,close_v=False)
