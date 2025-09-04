"""
Hallway Protocol Module
Deterministic multi-room session orchestrator with gate enforcement and audit trails
"""

from .hallway import HallwayOrchestrator, run_hallway
from .gates import GateDecision, GateInterface, CoherenceGate, evaluate_gate_chain
from .upcaster import upcast_v01_to_v02, downcast_v02_to_v01, verify_roundtrip
from .audit import canonical_json, sha256_hex, compute_step_hash, build_audit_chain

__all__ = [
    "HallwayOrchestrator",
    "run_hallway",
    "GateDecision",
    "GateInterface", 
    "CoherenceGate",
    "evaluate_gate_chain",
    "upcast_v01_to_v02",
    "downcast_v02_to_v01",
    "verify_roundtrip",
    "canonical_json",
    "sha256_hex",
    "compute_step_hash",
    "build_audit_chain"
]
