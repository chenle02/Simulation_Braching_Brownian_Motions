#!/usr/bin/env python3
#
# Created at Tue 23 Jan 2024 04:50:37 PM CST
#

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

import numpy as np
import matplotlib.pyplot as plt


class Branching_BM:
    def __init__(self, num_steps=1000, branching_prob=0.80, seed=42):
        """
        Initialize the Branching Brownian Motion simulation.

        :param num_steps: Number of steps in the simulation
        :param branching_prob: Probability of branching at each step
        :param seed: random seed
        """
        self.num_steps = num_steps
        self.branching_prob = branching_prob
        self.seed = seed
        self.positions = [np.zeros(num_steps)]

        # Initialize some state variables
        self.path_length = [num_steps]  # num_steps means the path is still alive
        self.final_length = 0
        self.num_paths = len(self.positions)

        # Set ten colors for each potential path
        self.colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'yellow', 'pink', 'brown', 'grey']

        # Set the random seed
        np.random.seed(self.seed)

    def Update_One_Path(self, path_id, step):
        """
        Update the specified path based on the branching and dying logic.

        This method applies the branching and dying logic to the path identified by path_id at the given simulation step. It determines whether the path should branch, continue, or die.

        :param path_id: The identifier of the path to be updated.
        :param step: The current step in the simulation process.
        :return: A boolean value; True if the path is still alive after this step, False if it has died.
        """
        alive = True
        if self.path_length[path_id] != self.num_steps:  # If path is dead, skip
            alive = False
            return alive

        action = np.random.choice(['branch', 'die'], p=[self.branching_prob, 1 - self.branching_prob])

        match action:
            case 'branch':
                self.positions.append(np.copy(self.positions[path_id]))  # Branching: duplicate the path
                self.path_length.append(self.num_steps)
            case 'die':
                alive = False
                self.path_length[path_id] = step  # Dying: record the path length

        return alive

    def simulate(self):
        """
        Run the simulation of the Brownian motion with branching.
        """
        for step in range(1, self.num_steps):
            for path_index in range(len(self.positions)):
                if self.path_length[path_index] == self.num_steps:  # If path is alive, update
                    if step % 100 == 0:
                        alive = self.Update_One_Path(path_index, step)
                        if not alive:
                            break
                    else:
                        self.positions[path_index][step] = self.positions[path_index][step - 1] + np.random.normal(scale=self.step_scale)

    def plot_paths(self):
        """
        Plot all the paths of the Brownian motions.
        """
        fig, ax = plt.subplots()
        # Plot each path
        for i in range(self.num_paths):
            # Plot up to the length of the current path
            ax.plot(range(self.path_length[i]), self.positions[i, :self.path_length[i]], color=self.colors[i % len(self.colors)])

        ax.set_title("Branching Brownian Motion Paths")
        ax.set_xlabel("Step")
        ax.set_ylabel("Position")
        plt.show()


BM = Branching_BM()
BM.simulate()
BM.plot_paths()