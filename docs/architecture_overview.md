# 4G vs 5G Mobile Network Architecture (High-Level)

```mermaid
flowchart LR

subgraph LTE_4G[4G LTE (E-UTRAN + EPC)]
  UE4G["UE (Phone)"] --> ENB["eNB"]
  ENB --> MME["MME (Control Plane)"]
  ENB --> SGW["SGW"]
  SGW --> PGW["PGW"]
  PGW --> INET4G["Internet"]
end

subgraph NR_5G[5G (NG-RAN + 5G Core)]
  UE5G["UE (Phone)"] --> GNB["gNB"]
  GNB --> AMF["AMF (Control Plane)"]
  GNB --> SMF["SMF"]
  SMF --> UPF["UPF"]
  UPF --> INET5G["Internet"]
end

