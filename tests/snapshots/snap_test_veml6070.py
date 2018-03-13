# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestVeml6070::test_disable 1'] = {
    'readlog': [
    ],
    'writelog': [
        (
            '56',
            [
                6,
                6,
                6
            ]
        )
    ]
}

snapshots['TestVeml6070::test_enable 1'] = {
    'readlog': [
    ],
    'writelog': [
        (
            '56',
            [
                6,
                6,
                6
            ]
        )
    ]
}

snapshots['TestVeml6070::test_integration_time 1'] = {
    'readlog': [
    ],
    'writelog': [
        (
            '56',
            [
                2,
                2,
                14
            ]
        )
    ]
}

snapshots['TestVeml6070::test_setup 1'] = {
    'readlog': [
    ],
    'writelog': [
        (
            '56',
            [
                6,
                6
            ]
        )
    ]
}

snapshots['TestVeml6070::test_uva_light_intensity 1'] = {
    'readlog': [
        (
            '56',
            [
                6,
                6
            ]
        ),
        (
            '57',
            [
                1,
                1
            ]
        )
    ],
    'writelog': [
        (
            '56',
            [
                6,
                6,
                6,
                6,
                14,
                14,
                14
            ]
        )
    ]
}

snapshots['TestVeml6070::test_uva_light_intensity_raw 1'] = {
    'readlog': [
        (
            '56',
            [
                52
            ]
        ),
        (
            '57',
            [
                18
            ]
        )
    ],
    'writelog': [
        (
            '56',
            [
                6,
                6,
                6,
                6
            ]
        )
    ]
}
