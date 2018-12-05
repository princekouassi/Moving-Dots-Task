###########################################################################################################
# Proportion dot task
###########################################################################################################
from __future__ import division
from __future__ import print_function
from psychopy import visual, event, core
import random, os

# Define a screen which is the size of the monitor
# win = visual.Window(fullscr=True,monitor="testMonitor",units="deg",blendMode='avg') # Full screen monitor
win = visual.Window((900, 700), allowGUI=False, monitor='testMonitor', units='deg') # Test screen monitor

###################################################
# Number of trials
###################################################
# The number of practice trials
npracticetrials = 5
# The number of test trials
ntesttrials = 1
###################################################

###################################################
# Different text
###################################################
intropracticetext = '''Introduction to practice trials here.''' # Introduction text for practice trials
introtesttext = ''' Introduction to test trials text here.''' # Introduction text for test trials 
breaktext = '''Take a break.''' # Break text
endpracticetext = '''Practice trials have now finished.''' # End of practice trial text
endtesttrialtext = '''You have finished.''' # End of test trial text
isitext = '''Press any key to begin the next trial.''' # Inter-trial text
###################################################

###################################################
# Practice Trials
###################################################

# Start by showing introduction text
while not event.getKeys(): 
 intropracticetext1 = visual.TextStim(win,text=intropracticetext,height=0.058,opacity=1.0,units='norm',contrast=1,pos=[0.0,0.0],color=1)
 intropracticetext1.draw()
 win.flip()

# TRIALS BEGIN HERE
for trials in range(npracticetrials): # Create loop to run the exact number of practice trials
    
    # Set the order of the conditions for each trial here (mainly the direction of the stimuli):
    usedconditions = random.randint(1,3) # Before every trial randomly pick one of three conditions
    print("Condition =",usedconditions) # functionality checking
    
    # Specify what each condition does (changes the speed of the stimuli):
    direction1a = 250 # Under patch for righ patch
    direction1b = 0 # Over patch for right patch
    direction2a = 250 # Under patch for left patch
    direction2b = 0 # Over patch for left patch
    if usedconditions == 1:
        direction1b=random.randint(1,360)
        direction2b = random.randint(1,360)
    elif usedconditions == 2:
        direction1b=random.randint(1,360)
        direction2b = random.randint(1,360)
    elif usedconditions == 3:
        direction1b=random.randint(1,360)
        direction2b = random.randint(1,360)
    
    # Seperate and put some text inbetween trials
    if trials > 0:
        while not event.getKeys():
         isitext1 = visual.TextStim(win,text=isitext,height=0.058,opacity=1.0,units='norm',contrast=1,pos=[0.0,0.0],color=1)
         isitext1.draw()
         win.flip()
    
    ############################
    # The right patch
    ############################
    # Initialize some stimuli for Patch 1A
    # UNDER PATCH
    dotPatch1A = visual.DotStim(win, color='white', dir=direction1a,
        nDots=85, fieldShape='sqr', fieldPos=(8.0, 0.0), fieldSize=6,
        dotLife=30,  # number of frames for each dot to be drawn
        signalDots='same',  # are signal dots 'same' on each frame? 
        noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
        speed=0.09, coherence=1,
        dotSize = 5)
    # Initialize some stimuli for Patch 1B (proportion patch)
    # oVER PATCH
    dotPatch1B = visual.DotStim(win, color='red', dir=direction1b,
        nDots=15, fieldShape='sqr', fieldPos=(8, 0.0), fieldSize=6,
        dotLife=30,  # number of frames for each dot to be drawn
        signalDots='same',  # are signal dots 'same' on each frame? 
        noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
        speed=0.09, coherence=1,
        dotSize = 5)
    #############################
    #############################
    
    #############################
    # The left patch
    #############################
    # Initialize some stimuli for Patch 2A
    # UNDER PATCH
    dotPatch2A = visual.DotStim(win, color='white', dir=direction2a,
        nDots=85, fieldShape='sqr', fieldPos=(-8, 0.0), fieldSize=6,
        dotLife=30,  # number of frames for each dot to be drawn
        signalDots='same',  # are signal dots 'same' on each frame? 
        noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
        speed=0.09, coherence=1,
        dotSize = 5)
    # Initialize some stimuli for Patch 2B (proportion patch)
    # OVER PATCH
    dotPatch2B = visual.DotStim(win, color='red', dir=direction2b,
        nDots=15, fieldShape='sqr', fieldPos=(-8, 0.0), fieldSize=6,
        dotLife=30,  # number of frames for each dot to be drawn
        signalDots='same',  # are signal dots 'same' on each frame?
        noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
        speed=0.09, coherence=1,
        dotSize = 5 )
    ##############################
    ##############################
    
    # Create clock to check stimulus presentation time
    stimuliclock = core.Clock()
    stimuliclock.reset()  # clock 
    Nframes = 60
    # Show the stimuli for 1 second using for loop on frames (60 frames equals 1 second)  
    for i in range(Nframes):
        dotPatch1A.draw()
        dotPatch1B.draw()
        dotPatch2A.draw()
        dotPatch2B.draw()
        stimulitimer= stimuliclock.getTime()
        win.flip()
    print ("Stimuli shown for", stimulitimer, "seconds")

# Need to clear the window before presenting the subsequent text
win.flip()

# End of practice trials so show text saying it is now over
endpracticetext1 = visual.TextStim(win,text=endpracticetext,height=0.058,opacity=1.0,units='norm',contrast=1,pos=[0.0,0.0],color=1)
endpracticetext1.draw()
win.flip()
core.wait(2.0) # Show the end text for 2 seconds
win.close()
core.quit()


