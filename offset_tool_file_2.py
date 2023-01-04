#___Writen by Animator: Nguyen Huyen Trang____________________________________________________________________________________________________________________
#___Lincense








#-------------------------------------------------------------------------------------------------------------------------------------------------------------
import maya.cmds as cmds

if cmds.window('lammotcaitool',exists=True):
    cmds.deleteUI('lammotcaitool')
    
def create_UI():
    cmds.window('lammotcaitool', title = 'OFFSET TOOL', w = 400, h= 600 )
    cmds.columnLayout(w=400,h=600,adj=0)
    
    cmds.text('CONTROLS')
    cmds.textFieldButtonGrp('name1',bl = 'Apply',bc = name_field1)
    cmds.textFieldButtonGrp('name2',bl = 'Apply',bc = name_field2)
    cmds.textFieldButtonGrp('name3',bl = 'Apply',bc = name_field3)
    cmds.textFieldButtonGrp('name4',bl = 'Apply',bc = name_field4)
    cmds.textFieldButtonGrp('name5',bl = 'Apply',bc = name_field5)
    cmds.textFieldButtonGrp('name6',bl = 'Apply',bc = name_field6)
    cmds.textFieldButtonGrp('name7',bl = 'Apply',bc = name_field7)
    cmds.textFieldButtonGrp('name8',bl = 'Apply',bc = name_field8)
    cmds.textFieldButtonGrp('name9',bl = 'Apply',bc = name_field9)
    cmds.textFieldButtonGrp('name10',bl = 'Apply',bc = name_field10)
    cmds.button('Delete locators', w= 160, h = 60, c = delete_locators, bgc = (1,1,1))
    
    cmds.intSliderGrp('number',l = 'Amplitude', min = 0, max = 20, f = 1, dc = value_number)
    
    
    
    cmds.showWindow('lammotcaitool')
    

create_UI()