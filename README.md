# MVP4 – Lichen Protocol Build Canon & Contracts

This repo contains the **MVP4 build canon**, contracts, and schemas for the Lichen Protocol system.

## 📂 Structure

- **build_canon/** – Canon-style governance protocols (Rooms, Orchestration, Gates, Diagnostics & Memory).
- **contracts/**  
  - **services/** – Machine-readable contracts for diagnostics and memory.  
  - **rooms/** – Contracts for PRA rooms.  
  - **gates/** – Contracts for output gates.  
  - **schema/** – JSON Schemas for validation.  
  - **types/** – Auto-generated TypeScript definitions (from schemas).  
- **package.json** – Validation & type generation scripts.

## 🛠️ Setup

Clone the repo and install dev dependencies:

```bash
git clone git@github.com:nzdog/MVP4.git
cd MVP4
npm install