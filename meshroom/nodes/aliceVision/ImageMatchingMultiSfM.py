import sys
import os
from meshroom.core import desc


class ImageMatchingMultiSfM(desc.CommandLineNode):
    commandLine = 'aliceVision_imageMatching {allParams}'
    # use both SfM inputs to define Node's size
    size = desc.MultiDynamicNodeSize(['input', 'inputB'])

    inputs = [
        desc.File(
            name='input',
            label='Input A',
            description='SfMData file .',
            value='',
            uid=[0],
        ),
        desc.File(
            name='inputB',
            label='Input B',
            description='SfMData file .',
            value='',
            uid=[0],
        ),
        desc.ListAttribute(
            elementDesc=desc.File(
                name="featuresFolder",
                label="Features Folder",
                description="",
                value="",
                uid=[0],
            ),
            name="featuresFolders",
            label="Features Folders",
            description="Folder(s) containing the extracted features and descriptors."
        ),
        desc.File(
            name='tree',
            label='Tree',
            description='Input name for the vocabulary tree file.',
            value=os.environ.get('ALICEVISION_VOCTREE', ''),
            uid=[0],
        ),
        desc.File(
            name='weights',
            label='Weights',
            description='Input name for the weight file, if not provided the weights will be computed on the database built with the provided set.',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='modeMultiSfM',
            label='Multiple SfM mode',
            description='Image matching multiple SfM mode.\n"a_ab" for images in input SfMData A plus between A and B.\n"a_b" for images between input SfMData A and B.',
            value='a_ab',
            values=['a_ab', 'a_b'],
            exclusive=True,
            uid=[0],
        ),
        desc.IntParam(
            name='minNbImages',
            label='Minimal Number of Images',
            description='Minimal number of images to use the vocabulary tree. If we have less features than this threshold, we will compute all matching combinations.',
            value=200,
            range=(0, 500, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='maxDescriptors',
            label='Max Descriptors',
            description='Limit the number of descriptors you load per image. Zero means no limit.',
            value=500,
            range=(0, 100000, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='nbMatches',
            label='Nb Matches',
            description='The number of matches to retrieve for each image (If 0 it will retrieve all the matches).',
            value=50,
            range=(0, 1000, 1),
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='verbosity level (fatal, error, warning, info, debug, trace).',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        )
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output List File',
            description='Filepath to the output file with the list of selected image pairs.',
            value=desc.Node.internalFolder + 'imageMatches.txt',
            uid=[],
        ),
        desc.File(
            name='outputCombinedSfM',
            label='Output Combined SfM',
            description='Path for the combined SfMData file',
            value=desc.Node.internalFolder + 'combineSfM.sfm',
            uid=[],
        ),
    ]
