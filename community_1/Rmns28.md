

### 1. CVE-2025-21293 – Exploit Público no Active Directory
- Vulnerabilidade crítica no Active Directory com PoC público, permitindo escalonamento de privilégios via Performance Counters (T1546).
- Detecções recomendadas:
  - Monitorar criação de subchaves em DnsCache e NetBT.
  - Rastrear adições a grupos privilegiados comumente vazios (T1098).
  - Fonte: SOC Prime :contentReference[oaicite:4]{index=4}.

### 2. MITRE ATT&CK® v17
- Lançamento da versão 17 em abril/2025:
  - Nova plataforma Enterprise: ESXi.
  - Renomeação de *Network* para *Network Devices*.
  - Agrupamento da técnica *Hijack Execution Flow: DLL Side-Loading* :contentReference[oaicite:5]{index=5}.
- Importância: foco atualizado, melhor cobertura de Virtualização.

### 3. MCP & “Trivial Trojans” – Ameaças em IA
- Ataques via protocol MCP permitem que agentes “confiáveis” cooperem para roubar dados, sem contar com infraestrutura complexa :contentReference[oaicite:6]{index=6}.
- Perigo: vetores emergentes em ambientes automatizados e IA-integrados.

---

###  Referências Úteis
- **MITRE ATT&CK** (base completa de técnicas/táticas): [ATT&CK Matrix] :contentReference[oaicite:7]{index=7}  
- **Workshop e tendências SOC Prime / ATT&CK**: apresentação sobre LLM-assisted Sigma rules e ATT&CK flows (Bruxelas, maio 2025) :contentReference[oaicite:8]{index=8}  
- **Detecção do CVE-2025-21293**: SOC Prime blog :contentReference[oaicite:9]{index=9}  
- **Atualização ATT&CK v17**: MITRE site :contentReference[oaicite:10]{index=10}  
- **Pesquisa MCP “Trivial Trojans”**: arXiv, julho 2025 :contentReference[oaicite:11]{index=11}  
