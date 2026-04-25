# Data Engineering — Reading Order

## Folder is currently empty

Free books in data engineering are scarce (most are paid O'Reilly titles). You can fill this folder by grabbing the free ones below.

## What to grab (FREE)

- **Data Engineering Cookbook** — Andreas Kretz — github.com/andkret/Cookbook — has PDF in repo
- **Spark: The Definitive Guide** — Chambers/Zaharia (free PDF after email at databricks.com)
- **Learning Spark (2e)** — Damji et al. (free PDF after email at databricks.com)
- **The Apache Kafka Definitive Guide** — Shapira et al. (free PDF at confluent.io)
- **I ❤ Logs** — Jay Kreps (free O'Reilly book, often hosted at confluent.io)
- **Streaming 101 + 102** — Tyler Akidau (free O'Reilly articles)
- **Mining of Massive Datasets** — already in `03-databases/` (covers big data algorithms)

## What's missing (PAID — must buy)

- **Designing Data-Intensive Applications** — Martin Kleppmann ⭐⭐⭐ (MUST OWN — covers DB + distributed + data eng)
- **Fundamentals of Data Engineering** — Reis/Housley ⭐⭐
- **Streaming Systems** — Akidau/Chernyak/Lax ⭐ (the streaming book)
- **The Data Warehouse Toolkit (3e)** — Kimball/Ross (dimensional modeling — old but foundational)
- **Data Pipelines Pocket Reference** — James Densmore
- **Stream Processing with Apache Flink** — Hueske/Kalavri
- **Data Engineering with Python** — Paul Crickard

## Path: Beginner → Advanced

### Foundations (4-6 weeks)
1. **Buy Fundamentals of Data Engineering** (Reis/Housley) — best modern overview
2. **Buy Designing Data-Intensive Applications** (Kleppmann) — read chapters 1-7 first
3. **SQL deep dive** — proper window functions, CTEs, query optimization

### Pipelines (4-8 weeks)
4. **Apache Airflow** — official tutorial → build a real DAG
5. **dbt** — getdbt.com tutorial → build a real warehouse
6. Basic ETL/ELT patterns: incremental, snapshot, change data capture

### Big data (when scale matters)
7. **Apache Spark** — Learning Spark book (free)
8. **Delta Lake / Iceberg / Hudi** — table formats
9. **Pandas → Polars → PySpark** — when each makes sense

### Streaming (advanced)
10. **Apache Kafka** — Definitive Guide (free)
11. **Apache Flink** OR **Kafka Streams** OR **Spark Structured Streaming**
12. **Streaming Systems** book (Akidau) — read this AFTER you've used streaming tools

### Storage & warehouses
13. **Snowflake / BigQuery / Redshift** — pick one for depth (docs)
14. **Object stores** — S3, GCS — partitioning, lifecycle policies

## Implementation milestones
- [ ] Build a real ETL pipeline with Airflow + dbt + Postgres
- [ ] Process 1 GB+ data in Spark (DataFrame API)
- [ ] Build a Kafka producer + consumer + transform with Streams
- [ ] Set up a streaming pipeline: Kafka → Flink → Iceberg
- [ ] Implement CDC from MySQL → Kafka with Debezium
- [ ] Build a dimensional model in dbt (facts + dimensions)
- [ ] Set up data quality checks (Great Expectations or dbt tests)

## Adjacent fields
- DB internals → `03-databases/`
- Distributed systems → `02-operating-systems/` + `06-system-design/`
- ML data prep → `21-mlops/`

## Reality check
Data engineering pay is excellent and demand is high. The boring secret: **most DE work is SQL + Airflow + dbt** — not Spark and Kafka. Master the boring stack first; reach for the streaming/big-data tools only when you actually need them.
