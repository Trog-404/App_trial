import datetime
import os
import random
import re
import time
from typing import TYPE_CHECKING, Dict, Iterable, List

import h5py
import numpy as np

import requests
from ase.data import atomic_masses, atomic_numbers, chemical_symbols
from unidecode import unidecode

from nomad.datamodel.metainfo.workflow import Link, Task, TaskReference, Workflow
from nomad.metainfo.data_type import m_str

if TYPE_CHECKING:
    from structlog.stdlib import (
        BoundLogger,
    )
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation
from nomad.metainfo import Quantity, Section, SubSection
from nomad.datamodel.metainfo.basesections import ProcessStep, Process


class FabricationStep(ProcessStep, EntryData):
    """
    Any dependant step of an `Activity`.
    """

    m_def = Section()
    fabricationEquipmentRecipeName = Quantity(
        type=str,
        description="""
        A short and descriptive name for the recipe used.
        """,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label='recipe name',
        ),
    )

class FabricationProcess(Process, EntryData, ArchiveSection):
    m_def = Section()
    fabricationProductType = Quantity(
        type=str,
        description="""
        A short and descriptive name for the product.
        """,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label='product name',
        ),
    )
    steps = SubSection(
        section_def = FabricationStep,
        repeats = True
    )
