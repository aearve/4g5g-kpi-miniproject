# 4G vs 5G Mobile Network Architecture (High-Level)

## 4G LTE (E-UTRAN + EPC)

```mermaid
flowchart LR
  UE[UE / Phone] --> eNB[eNodeB (4G RAN)]
  eNB --> MME[MME (Control Plane)]
  eNB --> SGW[SGW (User Plane)]
  SGW --> PGW[PGW (Internet Gateway)]
  PGW --> NET[(Internet)]
flowchart LR
  UE2[UE / Phone] --> gNB[gNodeB (5G RAN)]
  gNB --> AMF[AMF (Access & Mobility)]
  gNB --> SMF[SMF (Session Mgmt)]
  SMF --> UPF[UPF (User Plane)]
  UPF --> NET2[(Internet)]

---

### How to paste it (important)
- Click inside the **Terminal window**
- Press **⌘ Command + V** to paste  
  (Right-click does **not** work in nano)

---

### Then save & exit nano
1. **Control + O** → press **Enter**
2. **Control + X**

---

### After that
Type this and press Enter:

```bash
ls

