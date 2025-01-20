# Formazione Ansible Facts

Questo repository fornisce esercizi pratici per l'utilizzo dei moduli personalizzati di Ansible e l'arricchimento degli Ansible Facts. Gli esercizi guidano nella creazione di moduli Python per raccogliere informazioni sui sistemi target, con un focus particolare su utenti, gruppi e scadenze degli account.

## Contenuto

Gli esercizi sono suddivisi in tre step, ciascuno dei quali introduce nuove funzionalità e approfondimenti:

### **Step 1: Raccolta di Informazioni Base**
- Creazione di un modulo personalizzato che raccoglie:
  - Dati sugli utenti (es. username, UID, GID, home directory, shell).
  - Dati sui gruppi (es. nome del gruppo, GID, membri).
- Popolamento degli Ansible Facts:
  - `ansible_facts['users']` e `ansible_facts['users_by_uid']`.
  - `ansible_facts['groups']` e `ansible_facts['groups_by_gid']`.

### **Step 2: Arricchimento dei Facts con Gruppi**
- Estensione del modulo per:
  - Associare a ciascun utente il nome del gruppo principale.
  - Aggiungere i gruppi aggiuntivi a cui l'utente appartiene.
- Popolamento di facts aggiornati con informazioni più complete sugli utenti.

### **Step 3: Informazioni Avanzate**
- Supporto per sistemi Linux.
- Raccolta di informazioni di scadenza degli account (es. data di scadenza password e utente).
- Creazione di facts più avanzati per utenti e gruppi.

## Requisiti

- **Python** ≥ 3.8
- **Ansible** ≥ 2.10
- Sistema operativo:
  - **Step 1** e **Step 2**: Compatibili con Linux e macOS.
  - **Step 3**: Compatibile **solo** con Linux.

## Installazione

1. **Clonare il repository**:
   ```bash
   git clone https://github.com/<tuo-repo>/formazione_ansible_facts.git
   cd formazione_ansible_facts
   ```

2. **Installare Ansible** (se non presente):
   ```bash
   pip install ansible
   ```

3. **(Facoltativo) Creare un ambiente virtuale**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Esecuzione

Eseguire il playbook desiderato in base allo step:
   ```bash
   ansible-playbook -i localhost, test_playbook_step1.yml  # Per Step 1
   ansible-playbook -i localhost, test_playbook_step2.yml  # Per Step 2
   ansible-playbook -i localhost, test_playbook_step3.yml  # Per Step 3
   ```

## Output Atteso

I playbook popolano gli Ansible Facts con informazioni dettagliate sugli utenti e gruppi del sistema target. Consultare i singoli file README.md di ciascun step per esempi di output.

## Compatibilità

- **Step 1** e **Step 2**: Compatibili con Linux e macOS.
- **Step 3**: Compatibile **solo** con Linux (richiede il comando `chage`).

## Riferimenti

- Documentazione ufficiale Ansible
- Creazione di moduli personalizzati
