"""
Goal of Task 2:
    Derive speed feature from tracked data.
"""


import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from train import main_train
from bin.eval_velocity_influence import eval_velocity_influence
from bin.task2_prep import get_next_sample


class VelocityCalculator:
    # Defining __call__ method
    def __call__(self, sample=None, train_flag=False):
        """
        Function is executed on a call of the respective object e.g. example_object().

        inputs:
            sample (optional)
            train_flag (type: bool)

        given:
        previous_positions (type: np.ndarray, shape: (j, k, n)): with
            j: Length of tracked positions, e.g. 30 (= 30 timesteps observation)
            k: Batch size, e.g. 32 (= Number of trajectories for faster computing during training)
            n: Spatial dimension = 2, x-, y-Positions (relative coordinates)

        output:
            velocity array (type: np.ndarray, shape: (j, k)): with
                j: Length of tracking, so for every tracking step the associated velocity should be added
                k: Batch size, e.g. 32 (= Number of trajectories for faster computing during training)
        """

        if train_flag:
            previous_positions = sample
            t_hist = [np.arange(0, 3, 0.1)] * previous_positions.shape[1]
        elif sample is None:
            t_hist, previous_positions = get_next_sample()
        else:  # you can test your function over here (see below in __name__ == "__main__")
            t_hist, previous_positions = sample

        hist_len, n_batch, _ = previous_positions.shape

        velocity_array = np.zeros([hist_len, n_batch])
        n_interpolations = 3
        n_polyfit = 1

        # Task: Calculate the velocity from previous positions.
        ########################
        #  Start of your code  #
        ########################

        for n in range(n_batch):

            # Subtask 1: Extract two arrays for x and y from previous_positions and a array for t_obj from t_hist
            # Hints:
            # - shape of 'previous_positions' is History-length, Batch, Dimension (x, y),
            #   in our case: 30 x 1 x 2 (batch size of 1)
            # - 't_hist' is a list of arrays, each list for one batch, length auf each array is 30 (History-length)
            # ToDo: Uncomment the following lines and derive the desired values
            x_obj = []
            y_obj = []
            t_obj = []
            for n1 in range(0, 30):
                x_obj.append(previous_positions[n1][n][0])  # Dimension: (hist_len,)
                y_obj.append(previous_positions[n1][n][1])  # Dimension: (hist_len,)
                t_obj.append(t_hist[n])  # Dimension: (hist_len,)

            # Subtask 2:
            # Stack (np.vstack / np.stack) the x- and y-array. Determine the euclidean distance between successive
            # x-y-points (np.diff, np.linalg.norm, np.cumsum) and get dt timestep size as float (mean over t_obj).
            # Hint: After np.diff you will lose one dimension step (30 --> 29),
            #       so add an addtional value (0.0) at index [0] to get back to dimension 30.
            # ToDo: Uncomment the following lines and derive the desired values
            # xy_obj = np.stack([x_obj, y_obj], axis = 1)  # Dimension: (30, 2)
            # (np.diff, np.linalg.norm, np.cumsum)  # Dimension: (30, 2)
            s_obj = [0.0]
            dx = np.diff(x_obj)
            dy = np.diff(y_obj)
            dpos = np.stack([dx, dy], axis=0)
            s_obj.extend(np.cumsum(np.linalg.norm(dpos, axis=0), axis=0))
            # Dimension: (29,) --> (30,)
            dt_obj = [0.0]
            for n_dtobj in range(1, 30):
                dt_obj.append(s_obj[n_dtobj] / t_obj[0][n_dtobj])   # float
            # Subtask 3: Determine the speed feature: v = ds / dt (first derivation),
            #             use a filter (savgol_filter) to reduce noise.
            # Hint:
            #   - Doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html
            # ToDo: Uncomment the following lines and derive the desired values
            vel_obj = savgol_filter(x=dt_obj,
                                    window_length=n_interpolations,
                                    polyorder=n_polyfit,
                                    deriv=0,
                                    delta=1,)
            vel_obj.shape = (30,)

            # Subtask 4: Append vel_obj to velocity array
            # ToDo: Uncomment the following lines and derive the desired values
            for xx in range(0, 30):
                velocity_array[xx][n] = vel_obj[xx]  # Dimension: (30, n)
            pass

        # Subtask 5:
        # ToDo: Return velocity_array
        
        return velocity_array

        ########################
        #   End of your code   #
        ########################


def compare_performance(no_vel, with_vel):
    _, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    n_steps = np.arange(len(no_vel["nll"]))
    ax1.plot(n_steps, no_vel["nll"], label="without velocity")
    ax1.plot(n_steps, with_vel["nll"], label="with velocity")
    ax1.set_ylabel("NLL")
    ax1.grid(True)
    ax1.legend()

    n_steps = np.arange(len(no_vel["rmse"]))
    ax2.plot(n_steps, no_vel["rmse"], label="without velocity")
    ax2.plot(n_steps, with_vel["rmse"], label="with velocity")
    ax2.set_xlabel("timesteps (dt=0.1s)")
    ax2.set_ylabel("RMSE")
    ax2.grid(True)
    ax2.legend()

    plt.show()


def plot_results(velocity_array, ax):
    ax.cla()
    hist, batch = velocity_array.shape
    for b in range(batch):
        ax.plot(np.arange(hist), velocity_array[:, b], label="your solution")
        ax.legend()
        ax.set_xlabel("timesteps (dt=0.1s)", size=14)
        ax.set_ylabel("v in m/s", size=14)
        ax.grid(True)
        ax.axis("equal")

        plt.pause(1.0)


if __name__ == "__main__":
    vel = VelocityCalculator()
    tensor_output = vel()
    n_plots = 20

    for _ in range(n_plots):
        ax = plt.gca()
        velocity_array = vel()
        plot_results(velocity_array, ax)

    ########################
    #    Optional Task     #
    ########################
    # Check out the influence of the new feature on the prediction performance
    # Uncomment the following lines and let the training run
    # Check out the results regarding the RMSE and the NLL
    # NLL describes 'how sure the net is with the prediction'
    # RMSE is the root mean squared error
    # What do you think about the results?

    # # Uncomment and run the script
    # # Net Trainig without velocity feature
    # net_weights = main_train(full_train=True)
    # no_velocity_metrics = eval_velocity_influence(net_weights)

    # # Net Trainig with (your) velocity feature
    # vel = VelocityCalculator()
    # net_weights = main_train(vel, full_train=True)
    # with_velocity_metrics = eval_velocity_influence(net_weights, vel)

    # # Comparison
    # compare_performance(no_velocity_metrics, with_velocity_metrics)
