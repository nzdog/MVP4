"""
Hallway Protocol Module
Deterministic multi-room session orchestrator with gate enforcement and audit trails
"""

from .hallway import HallwayOrchestrator, run_hallway
from .gates import GateDecision, GateInterface, CoherenceGate, evaluate_gate_chain
from .upcaster import upcast_v01_to_v02, downcast_v02_to_v01, verify_roundtrip, map_room_output_to_v02, is_room_decline
from .audit import canonical_json, sha256_hex, compute_step_hash, build_audit_chain
from .rooms_registry import get_room_function, list_available_rooms, is_room_available, ROOMS
from .schema_utils import validate_room_output, validate_or_decline, create_schema_decline

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
    "map_room_output_to_v02",
    "is_room_decline",
    "canonical_json",
    "sha256_hex",
    "compute_step_hash",
    "build_audit_chain",
    "get_room_function",
    "list_available_rooms",
    "is_room_available",
    "ROOMS",
    "validate_room_output",
    "validate_or_decline",
    "create_schema_decline"
]
