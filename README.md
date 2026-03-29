# Hey, I'm Otavio Freindorfer 👋

IT Support Analyst transitioning into systems development. I work in Microsoft 365 environments at eNor Securities, but my real focus is building systems in **Rust** and **C++**.

---

## 🦀 What I'm Building

### Crypto Market Panel — Microservices Architecture in Rust

A fully functional market data platform designed from the ground up with microservice separation. I planned and architected the entire system; each service has a single responsibility and communicates through a central gateway.

```
┌─────────────────────────────────────────────────────────┐
│                     Web Frontend (JS)                    │
└───────────────────────┬─────────────────────────────────┘
                        │
              ┌─────────▼──────────┐
              │    Gateway API     │  ← single entry point for clients
              └──┬─────────────┬───┘
                 │             │
    ┌────────────▼───┐   ┌─────▼──────────────────┐
    │   Auth API     │   │  Analytics Candles      │
    │  (Rust/Argon2) │   │  Worker (OHLC engine)   │
    └────────────────┘   └─────────────┬───────────┘
                                       │
                          ┌────────────▼───────────┐
                          │  Trading Prices Worker  │
                          │  Coinbase · OKX ·       │
                          │  Google Finance         │
                          └────────────────────────┘
```

**Services:**
- `challenge-auth-api` — Session auth with encrypted credentials
- `challenge-trading-prices-worker` — Ingests live prices from 3 exchanges
- `challenge-analytics-candles-worker` — Computes OHLC candles across timeframes
- `challenge-gateway-api` — Edge API, routes frontend traffic to internal services
- `challenge-wealth-web` — Frontend: charts, order book panel, auth flow

---

## 🛠 Technologies

**Systems & Backend**
![Rust](https://img.shields.io/badge/Rust-000000?style=flat&logo=rust&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=postgresql&logoColor=white)

**Infrastructure & Tools**
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)

**IT & Cloud**
![Microsoft 365](https://img.shields.io/badge/Microsoft_365-D83B01?style=flat&logo=microsoft&logoColor=white)
![Azure](https://img.shields.io/badge/Entra_ID-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Intune](https://img.shields.io/badge/Intune-0078D4?style=flat&logo=microsoft&logoColor=white)

---

## 📌 About Me

- 🎓 Software Engineering student at Universidade Santo Amaro (2026–2030)
- 💼 IT Support Analyst @ eNor Securities — Microsoft 365, Entra ID, Intune
- 🧠 Interested in systems programming, backend architecture, and low-level design
- 📍 São Paulo, Brazil — open to remote opportunities
- 🔗 [LinkedIn](https://www.linkedin.com/in/otavio-v-freindorfer)

---

*Currently focused on deepening Rust knowledge and transitioning into a systems/backend developer role.*
