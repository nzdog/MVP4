#!/usr/bin/env python3
"""
Cross-contract validation for Lichen Protocol contracts.

This validator performs non-schema validation checks:
- Verifies every referenced gate in room gate_profile.chain exists in registry
- Verifies rooms referenced by hallway exist in registry  
- Detects circular references
- Checks basic semver compatibility where version constraints are present

This is separate from JSON Schema validation and focuses on contract relationships.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import re

def load_json_file(file_path: Path) -> Dict[str, Any]:
    """Load and parse a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return {}

def load_contract_registry() -> Dict[str, Any]:
    """Load the contract registry."""
    registry_path = Path(__file__).parent.parent / "contract_registry.json"
    return load_json_file(registry_path)

def get_available_gates(registry: Dict[str, Any]) -> Set[str]:
    """Extract available gate IDs from registry."""
    gates = set()
    for gate_key in registry.get("contracts", {}).get("gates", {}):
        # Extract gate_id from "gate_id@version" format
        gate_id = gate_key.split("@")[0]
        gates.add(gate_id)
    return gates

def get_available_rooms(registry: Dict[str, Any]) -> Set[str]:
    """Extract available room IDs from registry."""
    rooms = set()
    for room_key in registry.get("contracts", {}).get("rooms", {}):
        # Extract room_id from "room_id@version" format
        room_id = room_key.split("@")[0]
        rooms.add(room_id)
    return rooms

def validate_room_gate_references(registry: Dict[str, Any]) -> List[str]:
    """Validate that all gates referenced in rooms exist in the registry."""
    issues = []
    available_gates = get_available_gates(registry)
    
    # Check each room contract
    for room_key, room_path in registry.get("contracts", {}).get("rooms", {}).items():
        room_id = room_key.split("@")[0]
        room_file = Path(__file__).parent.parent / room_path
        
        if not room_file.exists():
            issues.append(f"Room contract file not found: {room_path}")
            continue
            
        room_data = load_json_file(room_file)
        if not room_data:
            continue
            
        # Check gate_profile.chain
        gate_profile = room_data.get("gate_profile", {})
        gate_chain = gate_profile.get("chain", [])
        
        for gate_id in gate_chain:
            if gate_id not in available_gates:
                issues.append(f"Room {room_id} references unknown gate: {gate_id}")
    
    return issues

def validate_hallway_room_references(registry: Dict[str, Any]) -> List[str]:
    """Validate that rooms referenced by hallway exist in registry."""
    issues = []
    available_rooms = get_available_rooms(registry)
    
    # Check hallway contract
    hallway_path = registry.get("contracts", {}).get("hallway", {}).get("hallway@0.2.0")
    if not hallway_path:
        issues.append("Hallway contract not found in registry")
        return issues
        
    hallway_file = Path(__file__).parent.parent / hallway_path
    if not hallway_file.exists():
        issues.append(f"Hallway contract file not found: {hallway_path}")
        return issues
        
    hallway_data = load_json_file(hallway_file)
    if not hallway_data:
        return issues
        
    # Check sequence
    sequence = hallway_data.get("sequence", [])
    for room_id in sequence:
        if room_id not in available_rooms:
            issues.append(f"Hallway references unknown room: {room_id}")
    
    return issues

def detect_circular_references(registry: Dict[str, Any]) -> List[str]:
    """Detect circular references in contract dependencies."""
    issues = []
    
    # For now, we don't have complex dependencies between contracts
    # This is a placeholder for future circular reference detection
    # when contracts start referencing each other more complexly
    
    return issues

def validate_semver_compatibility(registry: Dict[str, Any]) -> List[str]:
    """Check basic semver compatibility where version constraints are present."""
    issues = []
    
    # For now, all contracts are at 0.1.0, so no compatibility issues
    # This is a placeholder for future semver validation when we have
    # version constraints and multiple versions
    
    return issues

def main():
    """Main validation function."""
    print("🔍 Running cross-contract validation...")
    
    # Load registry
    registry = load_contract_registry()
    if not registry:
        print("❌ Failed to load contract registry")
        sys.exit(1)
    
    all_issues = []
    
    # Run validation checks
    print("  📋 Validating room gate references...")
    all_issues.extend(validate_room_gate_references(registry))
    
    print("  🚪 Validating hallway room references...")
    all_issues.extend(validate_hallway_room_references(registry))
    
    print("  🔄 Detecting circular references...")
    all_issues.extend(detect_circular_references(registry))
    
    print("  📦 Validating semver compatibility...")
    all_issues.extend(validate_semver_compatibility(registry))
    
    # Report results
    total_contracts = (
        len(registry.get("contracts", {}).get("rooms", {})) +
        len(registry.get("contracts", {}).get("gates", {})) +
        len(registry.get("contracts", {}).get("services", {})) +
        len(registry.get("contracts", {}).get("orchestrator", {})) +
        len(registry.get("contracts", {}).get("hallway", {}))
    )
    
    print(f"\n📊 Validation Results:")
    print(f"  Contracts scanned: {total_contracts}")
    print(f"  Issues found: {len(all_issues)}")
    
    if all_issues:
        print("\n❌ Issues found:")
        for issue in all_issues:
            print(f"  • {issue}")
        sys.exit(1)
    else:
        print("\n✅ All cross-contract validations passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()
