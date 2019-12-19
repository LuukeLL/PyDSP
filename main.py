#!/usr/bin/env python3
import scipy
from matplotlib import pyplot as plt


def main():
    # Source of this IQ File:
    # https://openofdm.readthedocs.io/en/
    wave = scipy.fromfile("IQSources/Samples.dat", dtype=scipy.int16)
    samples = [complex(i, q) for i, q in zip(wave[::2], wave[1::2])]

    plt.plot(samples)
    plt.show()


if __name__ == "__main__":
    main()