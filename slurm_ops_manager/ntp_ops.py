#!/usr/bin/env python3
"""This module provides the SlurmInstallManager."""
import logging
import subprocess
import sys

from ops.framework import (
    Object,
    StoredState,
)
from slurm_ops_manager.utils import OPERATING_SYSTEM


logger = logging.getLogger()



class CronyOpsManager(Object):
    """Chrony OpsManager."""

    _state = StoredState()

    def __init__(self):
        super().__init__()
        """Set the initial attribute values."""
        self._state.set_default(chrony_installed=False)

        self._install_chrony()

    def _install_chrony(self):
        if OPERATING_SYSTEM == 'ubuntu':
            try:
                subprocess.call([
                    "apt",
                    "install",
                    "chrony",
                    "-y",
                ])
            except subprocess.CalledProcessError as e:
                logger.debug(f"Cannot install chrony - {e}")
                sys.exit(-1)
        else:
            try:
                subprocess.call([
                    "yum",
                    "install",
                    "chrony",
                    "-y",
                ])
            except subprocess.CalledProcessError as e:
                logger.debug(f"Cannot install chrony - {e}")
                sys.exit(-1)
        self._state.chrony_installed = True


    @property
    def chrony_installed(self) -> bool:
        """Return the bool from the underlying _state."""
        return self._state.chrony_installed
