import matplotlib.pyplot as plt
import numpy as np

def potential(x) :
  energy = 0 
  forces = np.zeros([7,2])
  # Your code to calculate the potential goes here
  
  return energy, forces
  
# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This command reads in the velocities that are contained in the file called velocities.txt
vel = np.loadtxt( "velocities.txt" )

# This is the value to use for the timestep (the delta in the equations on the other side)
timestep = 0.005
# This calculates the initial values for the forces
eng, forces = potential(pos)

# We now run 500 steps of molecular dynamics
nsteps = 500
trajectory = np.zeros([int(nsteps/10),7,2])
for step in range(nsteps) :
  # First update the velocities a half timestep
  # fill in the blanks in the code here
  for i in range(7) : 
    vel[i][0] = 
    vel[i][1] = 
    
  # Now update the positions using the new velocities
  # You need to add code here
  
  
  # Recalculate the forces at the new position
  # You need to add code here
  eng, forces = 
  
  # And update the velocities another half timestep
  # You need to add code here


  # I have stored the trajectory here so we can plot how the positions 
  # of each of the atoms changes with time.  
  if step%10==0 : 
    for i in range(7) : 
      trajectory[int(step/10),i,0] = pos[i,0]
      trajectory[int(step/10),i,1] = pos[i,1]
 
# This will plot how position of the atoms during trajectory
cols = ['b.','r.','k.','g.','y.','c.','m.']
xd, yd = len(trajectory)*[0], len(trajectory)*[0]
for k in range(7) :
  for j in range(len(trajectory)) :
    xd[j], yd[j] = trajectory[j,k,0], trajectory[j,k,1]
  plt.plot( xd, yd, cols[k] )
plt.savefig( "trajectory.png" )
