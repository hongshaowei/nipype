# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ...testing import assert_equal
from ..c3 import C3dAffineTool

def test_C3dAffineTool_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fsl2ras=dict(argstr='-fsl2ras',
    position=4,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    itk_transform=dict(argstr='-oitk %s',
    hash_files=False,
    position=5,
    ),
    reference_file=dict(argstr='-ref %s',
    position=1,
    ),
    source_file=dict(argstr='-src %s',
    position=2,
    ),
    terminal_output=dict(nohash=True,
    ),
    transform_file=dict(argstr='%s',
    position=3,
    ),
    )
    inputs = C3dAffineTool.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_C3dAffineTool_outputs():
    output_map = dict(itk_transform=dict(),
    )
    outputs = C3dAffineTool.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

