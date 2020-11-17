import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_forces(self) : 
        pp = pos
        # Get the positions and analytic forces
        base_p, base_f = potential(pp)
        for i in range(7) :
            for j in range(2) :
                pp[i][j] = pp[i][j] + 1E-8
                new_p, crap = potential(pp)
                numder = (new_p-base_p)/1E-8
                self.assertTrue( np.abs(numder + base_f[i][j])<1e-4, "forces and potential are not consistent" )
                pp[i][j] = pp[i][j] - 1E-8
                
    def test_trajectory(self) :
        mypos = np.loadtxt("positions.txt")
        myvel = np.loadtxt("velocities.txt")
        eng, myforces = potential(mypos)

        fighand=plt.gca()
        this_x, this_y = np.zeros( [7,int(nsteps/10)] ), np.zeros( [7,int(nsteps/10)] )
        for j in range(7) :
            figdat = fighand.get_lines()[j].get_xydata()
            this_x[j], this_y[j] = zip(*figdat)

        for step in range(nsteps) :
            for i in range(7) : 
                myvel[i][0] = myvel[i][0] + 0.5*timestep*myforces[i][0]
                myvel[i][1] = myvel[i][1] + 0.5*timestep*myforces[i][1]
    
            for i in range(7) : 
                mypos[i][0] = mypos[i][0] + timestep*myvel[i][0]
                mypos[i][1] = mypos[i][1] + timestep*myvel[i][1]

            eng, myforces = potential(mypos)

            for i in range(7) : 
                myvel[i][0] = myvel[i][0] + 0.5*timestep*myforces[i][0]
                myvel[i][1] = myvel[i][1] + 0.5*timestep*myforces[i][1]
 
            if step%10==0 : 
               for i in range(7) :
                   self.assertTrue( np.abs( mypos[i][0] - this_x[i][int(step/10)] )<1E-4, "your trajectory is incorrect" )
                   self.assertTrue( np.abs( mypos[i][1] - this_y[i][int(step/10)] )<1E-4, "your trajectory is incorrect" )
