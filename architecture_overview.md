# 4G vs 5G Mobile Network Architecture (High-Level)

```mermaid
flowchart LR
  %% 4G LTE
  UE4G[UE (4G)] --> eNB[eNodeB]
  eNB --> MME
  eNB --> SGW
  SGW --> PGW
  PGW --> Internet4G[(Internet)]

  %% 5G
  UE5G[UE (5G)] --> gNB[gNodeB]
  gNB --> AMF
  gNB --> SMF
  SMF --> UPF
  UPF --> Internet5G[(Internet)]

