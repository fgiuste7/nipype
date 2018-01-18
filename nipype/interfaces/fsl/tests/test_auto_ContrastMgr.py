# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import ContrastMgr


def test_ContrastMgr_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        contrast_num=dict(argstr='-cope', ),
        corrections=dict(
            copyfile=False,
            mandatory=True,
        ),
        dof_file=dict(
            argstr='',
            copyfile=False,
            mandatory=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fcon_file=dict(argstr='-f %s', ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        output_type=dict(),
        param_estimates=dict(
            argstr='',
            copyfile=False,
            mandatory=True,
        ),
        sigmasquareds=dict(
            argstr='',
            copyfile=False,
            mandatory=True,
            position=-2,
        ),
        suffix=dict(argstr='-suffix %s', ),
        tcon_file=dict(
            argstr='%s',
            mandatory=True,
            position=-1,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = ContrastMgr.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ContrastMgr_outputs():
    output_map = dict(
        copes=dict(),
        fstats=dict(),
        neffs=dict(),
        tstats=dict(),
        varcopes=dict(),
        zfstats=dict(),
        zstats=dict(),
    )
    outputs = ContrastMgr.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
