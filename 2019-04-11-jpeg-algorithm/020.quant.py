#!/usr/bin/env python3
import cv2
import numpy as np
import scipy.fftpack as fftpack
from matplotlib import pyplot as plt
prev_16 = lambda x: x >> 4 << 4
quant = lambda: np.arange(4, 20) * np.arange(4, 20).reshape((-1, 1))


def encode_quant(orig):
    return (orig / quant().reshape((1, 16, 1, 16, 1))).astype(np.int8)


def decode_quant(orig):
    return orig * quant().reshape((1, 16, 1, 16, 1)).astype(float)


def encode_dct(orig):
    new_shape = (
        prev_16(orig.shape[0]),
        prev_16(orig.shape[1]),
        3
    )
    new = orig[
        :new_shape[0],
        :new_shape[1]
    ].reshape((
        new_shape[0] // 16,
        16,
        new_shape[1] // 16,
        16,
        3
    ))
    return fftpack.dctn(new, axes=[1,3], norm='ortho')


def decode_dct(orig):
    return fftpack.idctn(orig, axes=[1,3], norm='ortho'
    ).reshape((
        orig.shape[0]*16,
        orig.shape[2]*16,
        3
    ))


if __name__ == '__main__':
    im = cv2.imread("IMG_0108.JPG")
    enc = encode_dct(im)
    encq = encode_quant(enc)
    decq = decode_quant(encq)
    dec = decode_dct(decq)
    plt.imshow(dec.astype(np.uint8))
    plt.show()
    cv2.imwrite("IMG_0108_recompressed.png", dec.astype(np.uint8))
