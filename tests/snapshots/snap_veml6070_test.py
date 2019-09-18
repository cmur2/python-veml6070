# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestVeml6070::test_disable 1'] = [
    (
        'w',
        56,
        6
    ),
    (
        'w',
        56,
        7
    ),
    (
        'w',
        56,
        7
    )
]

snapshots['TestVeml6070::test_enable 1'] = [
    (
        'w',
        56,
        6
    ),
    (
        'w',
        56,
        7
    ),
    (
        'w',
        56,
        6
    )
]

snapshots['TestVeml6070::test_integration_time 1'] = [
    (
        'w',
        56,
        2
    ),
    (
        'w',
        56,
        3
    ),
    (
        'w',
        56,
        15
    )
]

snapshots['TestVeml6070::test_setup 1'] = [
    (
        'w',
        56,
        6
    ),
    (
        'w',
        56,
        7
    )
]

snapshots['TestVeml6070::test_uva_light_intensity 1'] = [
    (
        'w',
        56,
        6
    ),
    (
        'w',
        56,
        7
    ),
    (
        'w',
        56,
        6
    ),
    (
        'r',
        57,
        1
    ),
    (
        'r',
        56,
        6
    ),
    (
        'w',
        56,
        7
    ),
    (
        'w',
        56,
        15
    ),
    (
        'w',
        56,
        14
    ),
    (
        'r',
        57,
        1
    ),
    (
        'r',
        56,
        6
    ),
    (
        'w',
        56,
        15
    )
]

snapshots['TestVeml6070::test_uva_light_intensity_raw 1'] = [
    (
        'w',
        56,
        6
    ),
    (
        'w',
        56,
        7
    ),
    (
        'w',
        56,
        6
    ),
    (
        'r',
        57,
        18
    ),
    (
        'r',
        56,
        52
    ),
    (
        'w',
        56,
        7
    )
]
