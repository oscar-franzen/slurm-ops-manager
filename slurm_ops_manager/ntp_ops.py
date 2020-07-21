#!/usr/bin/env python3
"""This module provides the SlurmInstallManager."""
import logging
import subprocess
import sys

from slurm_ops_manager.utils import OPERATING_SYSTEM


class ChronyOpsManager:
    """ChronyOpsManager

    This class provides a public method that determines
    the operating system and installs the 'chrony' package
    using the appropriate package manager.
    """

    def __init__(self):
        self._logger = logging.getLogger()

    def install_chrony(self):
        """Determine the operating system and install chrony."""

        pkg_mgr = ""
        if OPERATING_SYSTEM == 'ubuntu':
            pkg_mgr = "apt"
        elif OPERATING_SYSTEM == 'centos':
            pkg_mgr = "yum"
        else:
            raise Exception(f"{OPERATING_SYSTEM} not supported")
            sys.exit(-1)

        try:
            subprocess.call([
                pkg_mgr,
                "install",
                "chrony",
                "-y",
            ])
        except subprocess.CalledProcessError as e:
            self._logger.debug(f"Cannot install chrony - {e}")
            sys.exit(-1)
