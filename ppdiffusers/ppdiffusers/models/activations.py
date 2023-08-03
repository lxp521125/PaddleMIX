import paddle.nn as nn


def get_activation(act_fn):
    if act_fn in ["swish", "silu"]:
        return nn.Silu()
    elif act_fn == "mish":
        return nn.Mish()
    elif act_fn == "gelu":
        return nn.GELU()
    else:
        raise ValueError(f"Unsupported activation function: {act_fn}")
