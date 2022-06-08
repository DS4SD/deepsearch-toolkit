from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


@dataclass
class ApiConnectedObject:
    api: CpsApi
