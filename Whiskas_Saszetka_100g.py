#!/usr/bin/python
'''
Script to run Houdini 15.5.673 with redshift on Windows 10
'''


# import importent liberys and houdini moduls
import sys
import argparse
# sys.path.append("C:/Program Files/Side Effects Software/Houdini 15.5.673/bin")
sys.path.append("C:/Program Files/Side Effects Software/Houdini 15.5.673/houdini/python2.7libs")
import hou

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help = "path to the image")
args = vars(ap.parse_args())

newName = args['input']

hou.hipFile.load('D:/Proj/MARS/HOU/Whiskas_Saszetka_100g_python_render_v01.hip')


def setTexture():
    # set new texture
    texturePath = "$HIP/tex/" + newName + ".tif"
    # assign new texture
    print texturePath
    shader1 = hou.parm("/shop/Packshot/Texture/tex0")
    shader1.set(texturePath)
    return;

def setRenderPath( str ):
    #set new render path
    renderPathF = "$HIP/render/" + str + "_Front.exr"
    renderPathP = "$HIP/render/" + str + "_Perspective.exr"
    renderPathGF = "$HIP/render/" + str + "_Ground_Front.exr"
    renderPathGP = "$HIP/render/" + str + "_Ground_Perspective.exr"
    renderPathAF = "$HIP/render/" + str + "_AO_Front.exr"
    renderPathAP = "$HIP/render/" + str + "_AO_Perspective.exr"

    # assign new render path
    renderF = hou.parm("/out/Redshift_Packshot_Front/RS_outputFileNamePrefix")
    renderF.set(renderPathF)

    renderP = hou.parm("/out/Redshift_Packshot_Perspective/RS_outputFileNamePrefix")
    renderP.set(renderPathP)

    renderGF = hou.parm("/out/Redshift_Ground_Front/RS_outputFileNamePrefix")
    renderGF.set(renderPathGF)

    renderGP = hou.parm("/out/Redshift_Ground_Perspective/RS_outputFileNamePrefix")
    renderGP.set(renderPathGP)

    renderAF = hou.parm("/out/Redshift_AO_Front/RS_outputFileNamePrefix")
    renderAF.set(renderPathAF)

    renderAP = hou.parm("/out/Redshift_AO_Perspective/RS_outputFileNamePrefix")
    renderAP.set(renderPathAP)





    return;

def startRenderFront():
    rnode = hou.node('/out/Redshift_Packshot_Front')
    rnode.render()
    return;


def startRenderPerspective():
    rnode = hou.node('/out/Redshift_Packshot_Perspective')
    rnode.render()
    return;

def startRenderGroundFront():
    rnode = hou.node('/out/Redshift_Ground_Front')
    rnode.render()
    return;

def startRenderGroundPerspective():
    rnode = hou.node('/out/Redshift_Ground_Perspective')
    rnode.render()
    return;

def startRenderAOFront():
    rnode = hou.node('/out/Redshift_AO_Front')
    rnode.render()
    return;

def startRenderAOPerspective():
    rnode = hou.node('/out/Redshift_AO_Perspective')
    rnode.render()
    return;

# def startRenderGroundPerspective():
#     rnode = hou.node('/out/Redshift_Packshot_Ground_Perspective')
#     rnode.render()
#     return;


setTexture()
setRenderPath(newName)
print "----- ----- ----- ----- ----- [ texture and render path done !!! ]"

startRenderFront()
startRenderPerspective()
print "----- ----- ----- ----- ----- [ Render Packshot done !!! ]"

startRenderGroundFront()
startRenderGroundPerspective()
print "----- ----- ----- ----- ----- [ Render Ground done !!! ]"

startRenderAOFront()
startRenderAOPerspective()
print "----- ----- ----- ----- ----- [ Render AO done !!! ]"


hou.hipFile.save("D:/Proj/MARS/HOU/Whiskas_Saszetka_100g_python_render_" + newName + ".hip")
exit();
