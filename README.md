# 📊 SMB Data Hub: Serverless ETL & Analytics Framework

## 🚀 Overview
A scalable, serverless data pipeline designed to extract, transform, and load (ETL) operational data from Small and Medium-sized Businesses (SMBs) into a centralized data warehouse. This framework bridges the gap between siloed business tools (e-commerce platforms, POS, booking systems) and enterprise-grade analytics, enabling local businesses to make data-driven decisions with zero infrastructure overhead.

## 💡 Business Value
Most SMBs generate valuable daily data but lack the technical infrastructure to leverage it. This project provides a modular, "plug-and-play" solution that:
- **Eliminates Manual Reporting:** Automates data extraction from various APIs (e.g., Shopify, Square, Calendly) directly into Google BigQuery.
- **Optimizes Operational Costs:** Utilizes a 100% serverless Google Cloud architecture, keeping maintenance and hosting costs near zero.
- **Drives Revenue Growth:** Powers real-time Looker Studio dashboards to track KPIs, identify high-margin products, and optimize sales strategies.

## 🛠️ Tech Stack & Architecture
- **Data Extraction:** Python (Requests, `dlt`, Custom API Wrappers)
- **Data Transformation:** Pandas / Polars
- **Data Warehouse:** Google BigQuery (SQL)
- **Orchestration:** Google Cloud Functions & Cloud Scheduler
- **Data Visualization:** Looker Studio / Power BI

## 🏗️ How It Works (Pipeline)
1. **Extract:** Python scripts pull daily records from client-specific APIs or Webhooks.
2. **Transform:** Data is cleaned, typed, and normalized in memory.
3. **Load:** The standardized data is pushed into BigQuery structured tables.
4. **Serve:** Live dashboards query the unified dataset to provide actionable insights.
