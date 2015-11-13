# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from .....testing import assert_equal
from ..brains import BRAINSMush

def test_BRAINSMush_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    boundingBoxSize=dict(argstr='--boundingBoxSize %s',
    sep=',',
    ),
    boundingBoxStart=dict(argstr='--boundingBoxStart %s',
    sep=',',
    ),
    desiredMean=dict(argstr='--desiredMean %f',
    ),
    desiredVariance=dict(argstr='--desiredVariance %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputFirstVolume=dict(argstr='--inputFirstVolume %s',
    ),
    inputMaskVolume=dict(argstr='--inputMaskVolume %s',
    ),
    inputSecondVolume=dict(argstr='--inputSecondVolume %s',
    ),
    lowerThresholdFactor=dict(argstr='--lowerThresholdFactor %f',
    ),
    lowerThresholdFactorPre=dict(argstr='--lowerThresholdFactorPre %f',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputMask=dict(argstr='--outputMask %s',
    hash_files=False,
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    outputWeightsFile=dict(argstr='--outputWeightsFile %s',
    hash_files=False,
    ),
    seed=dict(argstr='--seed %s',
    sep=',',
    ),
    terminal_output=dict(nohash=True,
    ),
    upperThresholdFactor=dict(argstr='--upperThresholdFactor %f',
    ),
    upperThresholdFactorPre=dict(argstr='--upperThresholdFactorPre %f',
    ),
    )
    inputs = BRAINSMush.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BRAINSMush_outputs():
    output_map = dict(outputMask=dict(),
    outputVolume=dict(),
    outputWeightsFile=dict(),
    )
    outputs = BRAINSMush.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

