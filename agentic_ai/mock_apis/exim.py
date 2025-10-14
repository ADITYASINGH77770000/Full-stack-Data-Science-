from __future__ import annotations
from typing import Dict, Any
import random

COUNTRIES = ["IN", "US", "CN", "DE", "BR", "ZA"]


def get_trade_trends(molecule: str) -> Dict[str, Any]:
    random.seed("exim-" + molecule)
    exports = {c: random.randint(100, 500) for c in COUNTRIES}
    imports = {c: random.randint(100, 500) for c in COUNTRIES}
    dependency = {c: round(imports[c] / max(exports[c], 1), 2) for c in COUNTRIES}
    return {
        "molecule": molecule,
        "exports_tonnes": exports,
        "imports_tonnes": imports,
        "import_dependency": dependency,
    }
