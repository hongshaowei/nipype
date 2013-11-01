# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.filtering.votingbinaryholefillingimagefilter import VotingBinaryHoleFillingImageFilter
def test_VotingBinaryHoleFillingImageFilter_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    foreground=dict(argstr='--foreground %d',
    ),
    radius=dict(argstr='--radius %s',
    sep=',',
    ),
    majorityThreshold=dict(argstr='--majorityThreshold %d',
    ),
    outputVolume=dict(position=-1,
    hash_files=False,
    argstr='%s',
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    background=dict(argstr='--background %d',
    ),
    inputVolume=dict(position=-2,
    argstr='%s',
    ),
    )
    inputs = VotingBinaryHoleFillingImageFilter.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_VotingBinaryHoleFillingImageFilter_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = VotingBinaryHoleFillingImageFilter.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
