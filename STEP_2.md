# Step 2

## Descrizione
Lo **Step 2** ha l'obiettivo di arricchire i dati raccolti nello **Step 1**, risolvendo e aggiungendo informazioni aggiuntive sui gruppi a cui gli utenti appartengono. In particolare, il modulo:
- Associa a ciascun utente il **nome del gruppo principale** (identificato dal GID dell'utente).
- Aggiunge una lista di **gruppi aggiuntivi** a cui l'utente appartiene, estratti dal file `/etc/group`.
  
Questo processo fornisce una visione più completa delle informazioni sugli utenti e sui gruppi presenti nel sistema.

Il modulo personalizzato di **Step 2**:
- Analizza i file `/etc/passwd` per ottenere i dettagli sugli utenti.
- Analizza i file `/etc/group` per ottenere i dettagli sui gruppi.
- Arricchisce i facts di Ansible aggiungendo al dizionario degli utenti:
  - Il **nome del gruppo principale**.
  - La lista dei **gruppi aggiuntivi** a cui l'utente appartiene.

I facts che vengono popolati includono:
- `ansible_facts['users']`: Dizionario con gli utenti, includendo il gruppo principale e i gruppi aggiuntivi.
- `ansible_facts['users_by_uid']`: Dizionario con gli UID degli utenti come chiavi, contenente le stesse informazioni arricchite.

## Struttura del Progetto

```bash
formazione_ansible_facts/
├── library/
│ └── user_group_facts_step2.py # Modulo personalizzato per arricchire i facts degli utenti e gruppi
├── test_playbook_step2.yml     # Playbook per testare il modulo
└── STEP_2.md                   # Documentazione di Step 2
```

## Requisiti

- **Python** ≥ 3.8 (Consigliato Python 3.13.1)
- **Ansible** ≥ 2.10 (Verificato con Ansible Core 2.18.1)

### Installazione di Ansible
Se Ansible non è installato, eseguire il seguente comando:
```bash
pip install ansible
```

## Guida all'Esecuzione

1. Clonare la repository (se necessario) ed entrare nella directory:
```bash
cd formazione_ansible_facts
```

2. Eseguire il playbook per raccogliere i facts arricchiti:
```bash
ansible-playbook -i localhost, test_playbook_step2.yml
```

3. Output atteso:
Dopo aver eseguito il playbook, i facts arricchiti verranno visualizzati in un formato simile a questo:
```yaml
"ansible_facts": {
    "users": {
        "root": {
            "uid": 0,
            "gid": 0,
            "primary_group": "root",
            "additional_groups": ["staff"]
        },
        "lucacisotto": {
            "uid": 501,
            "gid": 20,
            "primary_group": "staff",
            "additional_groups": ["admin", "staff"]
        }
    },
    "users_by_uid": {
        "0": {
            "uid": 0,
            "gid": 0,
            "primary_group": "root",
            "additional_groups": ["staff"]
        },
        "501": {
            "uid": 501,
            "gid": 20,
            "primary_group": "staff",
            "additional_groups": ["admin", "staff"]
        }
    }
}
```

## Risoluzione dei Problemi

- **Errore di Connessione SSH:**
Se si riceve un errore di connessione SSH come:
```bash
ssh: connect to host localhost port 22: Connection refused
```

Assicurati che il playbook venga eseguito in modalità locale aggiungendo questa riga al playbook:
```yaml
connection: local
```

## Riferimenti Utili

- Documentazione di Ansible sui moduli personalizzati
- Guida ufficiale di Ansible per la creazione di moduli personalizzati
