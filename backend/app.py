/ (repo root)
├─ README.md
├─ docker-compose.yml
├─ frontend/
│   ├─ package.json
│   ├─ next.config.js
│   ├─ tailwind.config.js
│   ├─ pages/
│   │   └─ index.jsx
│   ├─ components/
│   │   ├─ Header.jsx
│   │   └─ MapCard.jsx
│   └─ public/
│       └─ logo.svg
├─ backend/
│   ├─ app.py               # FastAPI
│   ├─ requirements.txt
│   └─ data/
│       ├─ fortnite_maps.json
│       └─ trainings.json
└─ infra/
    ├─ Dockerfile.backend
    └─ Dockerfile.frontend
