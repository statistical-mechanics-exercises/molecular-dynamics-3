# Generating a trajectory

The fact that we can now calculate the forces means we are in a position to write a molecular dynamics code and to generate our first trajectory.  We are going to be using the velocity Verlet algorithm to solve Newton's equation of motion.  I have given you a set of initial velocities for each of the atoms in the system (don't worry about how I generated these initial velocities.  You will learn how this is done next week).  The only other task that we have to do before we start the main trajectory loop is we have to calculate the potential energy of the initial configuration as well as the forces that are acting on each of the atoms in this initial configuration.  

Once these steps of initialisation are completed you then need to write a loop that performs the following four steps multiple times.  In this way your trajectory of positions is generated:

1. The velocities, ![](https://render.githubusercontent.com/render/math?math=v(t)), are updated by a half timestep using:

![](https://render.githubusercontent.com/render/math?math=v\left(t%2B\frac{1}{2}\delta\right)=v(t)%2B\frac{1}{2}\delta\F(t))

2. The positions, ![](https://render.githubusercontent.com/render/math?math=x(t)), are updated a full timestep using:

![](https://render.githubusercontent.com/render/math?math=x\left(t%2B\delta\right)=x(t)%2Bv\left(t%2B\frac{1}{2}\delta\right)\delta)

3. The forces, ![](https://render.githubusercontent.com/render/math?math=F(t%2B\delta)), are calculated at the new position.

4. The new values for the forces are used to update the velocities another half-timestep as follows:

![](https://render.githubusercontent.com/render/math?math=v\left(t%2B\delta\right)=v\left(t%2B\frac{1}{2}\delta\right)%2B\frac{1}{2}\delta\F(t%2B\delta))

Your task is to implement this algorithm in `main.py`.  As in the previous exercise, you need to start by writing a function called `potential` as you did in the previous exercise to calculate the potential and the forces.

You will then notice that I have written an outline for an MD code that computes a trajectory.  You need to complete this code by implementing the velocity Verlet algorithm that is described above.  You will notice that I have set up three Nx2 matrices to hold the positions (`pos`), velocities (`vel`) and forces (`forces`).  Notice that whenever you update the velocities, positions or forces in the velocity Verlet algorithm you never again need the old positions velocities or forces.  You thus can (and should) use these three matrices to hold the instantaneous positions, velocities and forces.  I have written some code that will keep track of the positions the atom adopts during the trajectory and that can be used to visualise what has occurred during the calculation.

The final result from your calculation should be a graph that shows the positions each of the atoms adopted during the trajectory.  

N.B Please note the variable timestep, ![](https://render.githubusercontent.com/render/math?math=\delta), in the algorithm described above should be set to a suitable value.  I have set it to a sensible value in the code to the right.  It is easy to tell if the value of the timestep is not sensible as total energy will not be conserved.      


