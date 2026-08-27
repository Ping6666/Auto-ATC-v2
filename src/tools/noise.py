import numpy as np
import matplotlib.pyplot as plt


def generate_and_plot_noise(savefig_fname):

    n_points = 5000

    x = np.random.randn(n_points)
    y = np.random.randn(n_points)

    plt.figure(figsize=(6, 6))

    plt.scatter(x, y, c='gray', s=5, alpha=0.6, edgecolors='none')

    plt.xlim(-4, 4)
    plt.ylim(-4, 4)

    plt.axis('off')
    # plt.grid(True, linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=300)
    plt.close('all')
    return


# Run the function
generate_and_plot_noise('./aaa.png')
