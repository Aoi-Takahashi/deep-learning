import numpy as np
from matplotlib import pyplot as plt

from model.activation import relu


def main():
    x = np.arange(-5.0, 5.0, 0.1)
    # y = step_function(x)
    # y = sigmoid(x)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y軸の範囲を指定
    # plt.savefig("figure/Step関数.png")
    # plt.savefig("figure/sigmoid.png")
    plt.savefig("figure/relu.png")


if __name__ == "__main__":
    main()
