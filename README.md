### Vision


#### Palantir-ing Myself
The vision of this application is to track as much data about myself as possible while learning new tech stacks.

#### Data I will collect
Complete:
- Body Weight
- New "Bests" in the Gym
Maybe One Day:
- Sleep 
- Basically anything is possible

#### Why this format for a gym app?
- The gym app market is very saturated, the idea behind privatizing my application was purely for the excused to use a dedicated linux pc, tailscale, and to get comfortable with real infrastructure.

#### Tech Stack

- Python 
  - Pandas
  - matplotlib
  - pydantic
  
- FastAPI
- Virtual Environment
- Apple Shortcuts for sending user data
- Tailscale + Server for network tunnelling and recieving data

---

### Demo (GitHub Pages)

A static demo is deployed at:

**https://hub-ry.github.io/protocol-demo/**

The demo uses embedded sample data. To run the full app with your own backend (e.g. local or Tailscale server), set `VITE_API_URL` when building or running the frontend (e.g. `VITE_API_URL=http://localhost:5000` or your server URL).

---

Personal Notes:

``venv/bin/uvicorn src.main:app --host 0.0.0.0 --port 5000``
