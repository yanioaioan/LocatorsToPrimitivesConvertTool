import maya.cmds as cmds

'''selects 5000 locators in the scene, queries their positions for each frame in the range 1-150
 and converts them into primitive spheres with the corresponding keyframed positions'''

framelocatorsPositionsAtFrame=[]
locatorsPositionsAtFrame=[]
frame=1
keyframes=[]
for f in range(1,151,1):#for each frame
	cmds.currentTime( f )
	locatorsPositionsAtFrame=[]
	print 'stuffing-quering locators positions from frame %d ...'%(f)
	for i in range(5000):#for each locator
				
		#take save its position at this frame
		locatorsPositionsAtFrame.append(cmds.xform('locator'+str(i) ,translation=True, query=True))
		#print 'frame%d: Store locator\'s%d position'%(f,i)
	framelocatorsPositionsAtFrame.append(locatorsPositionsAtFrame)#save 5000 locator positions at each frame
	#len(locatorsPositionsAtFrame)
	#len(framelocatorsPositionsAtFrame)

#precreate a vector of 150*5000 spheres
totalparticles=5000#150
for i in range(totalparticles):
	cmds.polySphere()
	cmds.scale(0.02,0.02,0.02)


frameNumber=0
for i in framelocatorsPositionsAtFrame:#for each frame
	#print len(i)	
	frameNumber+=1
	print 'converting locators from frame %d ...'%(frameNumber)
	cmds.currentTime( frameNumber )
	for j in range(totalparticles):#for each position set
		#print 'at frame%d Sphere%d pos=%s '%(frameNumber,j,i[j])
		#print 'pSphere'+str(j+1)
		
		#move the j+1sphere
		cmds.select( 'pSphere'+str(j+1))
		cmds.move(i[j][0], i[j][1], i[j][2])
		cmds.setKeyframe()
	
'''	
	print cmds.keyframe( 'pSphere1.translateZ', time=(3,3), query=True)

	#cmds.delete('locator'+str(i))


for pos in locatorPositions:
	cmds.polySphere()
	cmds.scale(0.05,0.05,0.05)
	cmds.move(pos[0],pos[1],pos[2])
	
	
for t in range(1,2,1):
	cmds.currentTime( t )
	
	#for each locator for this frame
	locatorsPositions=[]
	for i in range(5000):
		cmds.xform('locator'+str(i) ,translation=True, query=True)
		locatorPositions.append(cmds.xform('locator'+str(i) ,translation=True, query=True))
	frameLocatorPosition.append(locatorPositions)
	
'''
