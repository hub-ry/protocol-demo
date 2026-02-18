### Vision


#### Palantir-ing Myself
The vision of this application is to track as much data about myself as possible while learning new tech stacks.

#### Data I will collect
- Body Weight
- Sleep Habits
- Reps and Weight of gym exercises
- Nutrition


#### Graphing and gathering data
I will graph this data and analyze the results.


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
