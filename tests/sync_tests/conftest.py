#    Copyright Frank V. Castellucci
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# -*- coding: utf-8 -*-

"""Fixtures for testing."""

import subprocess
import pytest

from pysui.sui.sui_clients.sync_client import SuiClient
from pysui.sui.sui_config import SuiConfig

LOCALNET_PROC_REGEN: str = ["bash", "localnet", "regen"]
LOCALNET_PROC_STOP: str = ["bash", "localnet", "stop"]


# @pytest.fixture(scope="session")
def sui_base_localnet_start() -> bool:
    """."""
    result = subprocess.run(LOCALNET_PROC_REGEN, capture_output=True, text=True)
    if result.returncode == 0:
        return True
    raise ValueError(f"Result of localnet regen {result.stderr}")


# @pytest.fixture(scope="session")
def sui_base_localnet_stop() -> bool:
    """."""
    result = subprocess.run(LOCALNET_PROC_STOP, capture_output=True, text=True)
    if result.returncode == 0:
        return True
    raise ValueError(f"Result of localnet stop {result.stderr}")


@pytest.fixture(scope="session")
def sui_client() -> SuiClient:
    """."""
    sui_base_localnet_start()
    client = SuiClient(SuiConfig.sui_base_config())
    yield client
    sui_base_localnet_stop()
