# input: 5

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print( (c*(2*i+1)).center(2*thickness - 1,' ') )

#Top Pillars
for i in range(thickness+1):
    print( (c*thickness).center(2*thickness - 1,' ') , end='' )
    print( (c*thickness).rjust(4*thickness - thickness//2,' ') )
    
#Middle Belt
for i in range((thickness+1)//2):
    print( (c*thickness*5).rjust(thickness*5 + thickness//2,' ') ) 
    
#Bottom Pillars
for i in range(thickness+1):
    print( (c*thickness).center(2*thickness - 1,' ') , end='' )
    print( (c*thickness).rjust(4*thickness - thickness//2,' ') )
    
#Bottom Cone
for i in reversed(range(thickness)): 
    print( ' '*(4*thickness) , end='' ) #+ thickness//2
    print( (c*(2*i+1)).center(2*thickness - 1,' ') )
