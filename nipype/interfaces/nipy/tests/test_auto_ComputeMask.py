# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import ComputeMask

def test_ComputeMask_inputs():
    input_map = dict(M=dict(),
    cc=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    m=dict(),
    mean_volume=dict(mandatory=True,
    ),
    reference_volume=dict(),
    )
    inputs = ComputeMask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ComputeMask_outputs():
    output_map = dict(brain_mask=dict(),
    )
    outputs = ComputeMask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

