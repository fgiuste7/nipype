# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import Hist


def test_Hist_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bin_width=dict(argstr='-binwidth %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-input %s',
    copyfile=False,
    mandatory=True,
    position=1,
    ),
    mask=dict(argstr='-mask %s',
    ),
    max_value=dict(argstr='-max %f',
    ),
    min_value=dict(argstr='-min %f',
    ),
    nbin=dict(argstr='-nbin %d',
    ),
    out_file=dict(argstr='-prefix %s',
    keep_extension=False,
    name_source=[u'in_file'],
    name_template='%s_hist',
    ),
    out_show=dict(argstr='> %s',
    keep_extension=False,
    name_source='in_file',
    name_template='%s_hist.out',
    position=-1,
    ),
    showhist=dict(argstr='-showhist',
    usedefault=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Hist.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Hist_outputs():
    output_map = dict(out_file=dict(),
    out_show=dict(),
    )
    outputs = Hist.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
