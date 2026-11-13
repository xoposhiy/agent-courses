"""SatIR and VERDICT from FORMA (external/trial-forma).

Both are part of a clinical-trial formal-reasoning pipeline that needs licensed
ontologies (SNOMED CT, UMLS), running Elasticsearch + Snowstorm services and a
compiled ``build/`` of SMT programs before anything can run. None of that is in
the checkout, so these workers report themselves unavailable with the reason;
the orchestrator then routes retrieval and criteria-based decisions to the
coding agent.
"""

from __future__ import annotations

from pathlib import Path

from ..tasks import Step
from ..worker import StepFailed
from ..workspace import Workspace
from .base import ExternalCapability


class _FormaCapability(ExternalCapability):
    repo = "trial-forma"
    #: Artifacts the FORMA pipeline consumes; produced by its offline compile steps.
    needs: tuple[str, ...] = ()

    def available(self) -> tuple[bool, str]:
        ok, why = super().available()
        if not ok:
            return ok, why
        missing = [p for p in self.needs if not (self.repo_dir / p).exists()]
        if missing:
            return False, (f"FORMA build artifacts missing ({', '.join(missing)}); they require SNOMED CT/UMLS "
                           "licenses plus Elasticsearch and Snowstorm services to compile")
        return True, ""

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        raise StepFailed(f"{self.name} cannot run here: {self.available()[1]}")


class SatIR(_FormaCapability):
    name = "satir"
    needs = ("build/trial.db",)
    description = (
        "SatIR: high-recall retrieval of clinical trials for a patient from FORMA's relational "
        "projection of compiled trial criteria (SQL over ontology-closed concept sets). "
        "instructions = the patient id; inputs = the compiled trial database."
    )


class Verdict(_FormaCapability):
    name = "verdict"
    needs = ("build/noslice_ir_linked",)
    description = (
        "VERDICT: evidence-based eligibility decisions of a patient against explicit trial criteria "
        "compiled to SMT (z3), with unsat-core rationales. instructions = trial id and patient id; "
        "inputs = the patient note JSON and the compiled trial programs."
    )
