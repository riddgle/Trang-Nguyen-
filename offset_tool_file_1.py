import maya.cmds as cmds
def value_number(*args):
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)

def locator_gr(*args):
    cmds.CreateLocator(name = 'locator1')
    cmds.CreateLocator(name = 'locator2')
    cmds.CreateLocator(name = 'locator3')
    cmds.CreateLocator(name = 'locator4')
    cmds.CreateLocator(name = 'locator5')
    cmds.CreateLocator(name = 'locator6')
    cmds.CreateLocator(name = 'locator7')
    cmds.CreateLocator(name = 'locator8')
    cmds.CreateLocator(name = 'locator9')
    cmds.CreateLocator(name = 'locator10')
locator_gr()
    
def name_field1(*args):
    textfieldBt1 = cmds.textFieldButtonGrp('name1', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt1)
        print(textfieldBt1)
    cmds.orientConstraint([textfieldBt1],'locator1',w=1)
    cmds.select('locator1')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.select('locator1_orientConstraint1')
    cmds.delete('locator1_orientConstraint1')
    cmds.orientConstraint('locator1',[textfieldBt1],w=1)
    cmds.select([textfieldBt1])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    
    
def name_field2(*args):
    textfieldBt2 = cmds.textFieldButtonGrp('name2', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt2)
        print(textfieldBt2)
    
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator1'],['locator2'],w=1)
    cmds.select('locator2')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+1)
    cmds.select('locator2_orientConstraint1')
    cmds.delete('locator2_orientConstraint1')
    cmds.orientConstraint('locator2',[textfieldBt2],w=1)
    cmds.select([textfieldBt2])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    
def name_field3(*args):
    textfieldBt3 = cmds.textFieldButtonGrp('name3', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt3)
        print(textfieldBt3)
    
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator2'],['locator3'],w=1)
    cmds.select('locator3')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+2)
    cmds.select('locator3_orientConstraint1')
    cmds.delete('locator3_orientConstraint1')
    cmds.orientConstraint('locator3',[textfieldBt3],w=1)
    cmds.select([textfieldBt3])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    
def name_field4(*args):
    textfieldBt4 = cmds.textFieldButtonGrp('name4', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt4)
        print(textfieldBt4)
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator3'],['locator4'],w=1)
    cmds.select('locator4')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+3)
    cmds.select('locator4_orientConstraint1')
    cmds.delete('locator4_orientConstraint1')
    cmds.orientConstraint('locator4',[textfieldBt4],w=1)
    cmds.select([textfieldBt4])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)

    
def name_field5(*args):
    textfieldBt5 = cmds.textFieldButtonGrp('name5', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt5)
        print(textfieldBt5)
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator4'],['locator5'],w=1)
    cmds.select('locator5')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+4)
    cmds.select('locator5_orientConstraint1')
    cmds.delete('locator5_orientConstraint1')
    cmds.orientConstraint('locator5',[textfieldBt5],w=1)
    cmds.select([textfieldBt5])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
   
    
def name_field6(*args):
    textfieldBt6 = cmds.textFieldButtonGrp('name6', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt6)
        print(textfieldBt6)
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator5'],['locator6'],w=1)
    cmds.select('locator6')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+5)
    cmds.select('locator6_orientConstraint1')
    cmds.delete('locator6_orientConstraint1')
    cmds.orientConstraint('locator6',[textfieldBt6],w=1)
    cmds.select([textfieldBt6])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
   
    
def name_field7(*args):
    textfieldBt7 = cmds.textFieldButtonGrp('name7', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt7)
        print(textfieldBt7)
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator6'],['locator7'],w=1)
    cmds.select('locator7')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+6)
    cmds.select('locator7_orientConstraint1')
    cmds.delete('locator7_orientConstraint1')
    cmds.orientConstraint('locator7',[textfieldBt7],w=1)
    cmds.select([textfieldBt7])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
 
    
def name_field8(*args):
    textfieldBt8 = cmds.textFieldButtonGrp('name8', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt8)
        print(textfieldBt8)
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator7'],['locator8'],w=1)
    cmds.select('locator8')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+7)
    cmds.select('locator8_orientConstraint1')
    cmds.delete('locator8_orientConstraint1')
    cmds.orientConstraint('locator8',[textfieldBt8],w=1)
    cmds.select([textfieldBt8])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    
            
def name_field9(*args):
    textfieldBt9 = cmds.textFieldButtonGrp('name9', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt9)
        print(textfieldBt9)
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator8'],['locator9'],w=1)
    cmds.select('locator9')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+8)
    cmds.select('locator9_orientConstraint1')
    cmds.delete('locator9_orientConstraint1')
    cmds.orientConstraint('locator9',[textfieldBt9],w=1)
    cmds.select([textfieldBt9])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
  
    
def name_field10(*args):
    textfieldBt10 = cmds.textFieldButtonGrp('name10', q = True, tx = True)
    objects = cmds.ls(sl = True)
    for i in objects:
        cmds. select(textfieldBt10)
        print(textfieldBt10)
    my_value = cmds.intSliderGrp('number', value = True, q = True)
    n = int(my_value)
    cmds.orientConstraint(['locator9'],['locator10'],w=1)
    cmds.select('locator10')
    start = cmds.playbackOptions(q=1,min=1)
    end = cmds.playbackOptions(q=1,max=1)
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
    cmds.selectKey(add = 1, k = 1, attribute =('translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
    cmds.keyframe(edit=1,iub = True,r = 1, tc=n+9)
    cmds.select('locator10_orientConstraint1')
    cmds.delete('locator10_orientConstraint1')
    cmds.orientConstraint('locator10',[textfieldBt10],w=1)
    cmds.select([textfieldBt10])
    cmds.bakeResults(sm=True,t=(start,end),sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,bol=False, mr=True,cp=False,s=True)
  
def delete_locators(*args):
    delete_locators = cmds.ls('locator*')
    if len(delete_locators)>0:
        cmds.delete(delete_locators)

 
 
