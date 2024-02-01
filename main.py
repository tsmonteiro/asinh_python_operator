from tercen.client import context as ctx
import numpy as np
import math
import polars as pl


#http://127.0.0.1:5400/test/w/5409bc1875748e715c48848fd3004e42/ds/b01374e4-0faa-43d1-8e78-a4e349e1e0d2
tercenCtx = ctx.TercenContext()

def transform_and_scale(x, scale):
    return math.asinh(x/scale)


scale = tercenCtx.operator_property('scale', typeFn=int, default=5)

df = tercenCtx.select(['.y', '.ci', '.ri'])

df = df.with_columns(asinh=pl.col(".y") / scale).drop(".y")

df = tercenCtx.add_namespace(df) 
tercenCtx.save(df)
