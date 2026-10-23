# 📊 B2B Tech Founders, CEOs & Investor Lead Dataset

[![Dataset: Verified](https://img.shields.io/badge/Dataset-Verified%20Contacts-green.svg)](https://github.com/whyst0ne/b2b-tech-founders-leads)
[![Format: CSV / JSON](https://img.shields.io/badge/Format-CSV%20%7C%20JSON-blue.svg)](https://github.com/whyst0ne/b2b-tech-founders-leads)
[![x402 Enabled](https://img.shields.io/badge/x402-Pay--Per--Lead%20API-6f42c1.svg)](https://github.com/whyst0ne/webomni-api)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?style=flat&logo=github)](https://github.com/sponsors/whyst0ne)

A curated, continuously enriched directory of technology startup founders, C-suite executives, angel investors, and venture partners designed for outbound B2B growth, recruiting, and AI agent workflows.

---

## 📁 Repository Assets

- [`b2b_tech_leads.csv`](./b2b_tech_leads.csv) — Clean comma-separated dataset ready for CRM import (HubSpot, Salesforce, Apollo, Pipedrive).
- [`b2b_tech_leads.json`](./b2b_tech_leads.json) — Structured JSON records for programmatic and LLM agent ingestion.
- [`lead_engine.py`](./lead_engine.py) — Automated verification, deduplication, and enrichment script triggered weekly via GitHub Actions.

---

## 📋 Data Schema

| Field | Description | Example |
|---|---|---|
| `name` | Executive / Founder Full Name | `Sarah Chen` |
| `title` | Position / Role | `Co-Founder & CEO` |
| `company` | Organization Name | `NeuralScale AI` |
| `industry` | Primary Tech Vertical | `Generative AI / Infrastructure` |
| `email` | Primary Verified Work Email | `sarah.chen@neuralscale.ai` |
| `phone` | Direct Office / Contact Phone | `+1 (415) 555-0142` |
| `linkedin` | Professional Profile URL | `https://linkedin.com/in/sarahchen-ai` |
| `city` | Geographic Hub | `San Francisco, CA` |
| `country` | Country | `United States` |

---

## 🤖 On-Demand Enrichment via WebOmni API & x402
Need real-time domain scraping, custom vertical filtering, or automated AI agent access?
- **Companion Micro-SaaS:** 👉 **[WebOmni API](https://github.com/whyst0ne/webomni-api)**
- **MCP Agent Server & x402 Settlement:** Autonomous agents can query enriched datasets on-demand with permissionless USDC micro-payments on Base/Arbitrum.

---

## 💳 Direct Web3 Settlement & Custom Dataset Orders
For custom enterprise exports (50,000+ verified tech decision-makers) or direct on-chain settlement:
- **EVM Wallet (Base / Arbitrum / Polygon / Optimism / Ethereum):** `0xE5Ab26877172254B72f3AE6DA5789D2468B7B282`
- **Supported Assets:** `USDC`, `USDT`, `DAI`, `ETH`

Published and maintained by [whyst0ne](https://github.com/whyst0ne).
