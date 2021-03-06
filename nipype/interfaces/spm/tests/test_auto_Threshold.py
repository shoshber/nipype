# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import Threshold


def test_Threshold_inputs():
    input_map = dict(contrast_index=dict(mandatory=True,
    ),
    extent_fdr_p_threshold=dict(usedefault=True,
    ),
    extent_threshold=dict(usedefault=True,
    ),
    force_activation=dict(usedefault=True,
    ),
    height_threshold=dict(usedefault=True,
    ),
    height_threshold_type=dict(usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    paths=dict(),
    spm_mat_file=dict(copyfile=True,
    mandatory=True,
    ),
    stat_image=dict(copyfile=False,
    mandatory=True,
    ),
    use_fwe_correction=dict(usedefault=True,
    ),
    use_mcr=dict(),
    use_topo_fdr=dict(usedefault=True,
    ),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    )
    inputs = Threshold.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Threshold_outputs():
    output_map = dict(activation_forced=dict(),
    cluster_forming_thr=dict(),
    n_clusters=dict(),
    pre_topo_fdr_map=dict(),
    pre_topo_n_clusters=dict(),
    thresholded_map=dict(),
    )
    outputs = Threshold.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
