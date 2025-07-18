# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
from niworkflows.interfaces.bids import DerivativesDataSink as _DDSink

from .cifti import GeneratePetCifti
from .tacs import ExtractRefTAC, ExtractTACs


class DerivativesDataSink(_DDSink):
    out_path_base = ''


__all__ = (
    'DerivativesDataSink',
    'GeneratePetCifti',
    'ExtractTACs',
    'ExtractRefTAC',
)
