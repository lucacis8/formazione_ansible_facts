# Step 3 - Raccolta avanzata di facts su utenti e gruppi

Questo step estende la raccolta di facts includendo informazioni avanzate sugli utenti di sistema, i gruppi e la data di scadenza degli account.

**Nota:** A differenza degli Step 1 e 2, questo step è compatibile solo con sistemi Linux (es. Ubuntu) e **non** è supportato su macOS.

## Requisiti

- Sistema operativo Linux (Ubuntu 22.04 o superiore)
- Python 3
- Ansible

## Installazione

1. **Aggiornare il sistema**

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Installare Python, pip e Ansible (se non presenti)**

   ```bash
   sudo apt install python3 python3-pip python3-venv ansible -y
   ```

3. **Creare e attivare un ambiente virtuale**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Installare eventuali dipendenze Python**

   ```bash
   pip install -r requirements.txt
   ```

## Struttura del progetto

```bash
formazione_ansible_facts/
├── library/
│   └── user_group_facts_step3.py       # Modulo personalizzato Ansible
├── test_playbook_step3.yml             # Playbook di test per Step 3
├── requirements.txt                    # Dipendenze Python (se necessario)
└── STEP_3.md                           # Documentazione
```

## Esecuzione del playbook

Per eseguire il playbook e raccogliere i facts avanzati:

   ```bash
   ansible-playbook -i localhost, test_playbook_step3.yml
   ```

## Esempio di output

```json
{
    "users": [
        {
            "name": "luca-cisotto",
            "uid": 1000,
            "gid": 1000,
            "home": "/home/luca-cisotto",
            "shell": "/bin/bash",
            "expiry": "N/A"
        }
    ],
    "groups": [
        {
            "name": "sudo",
            "gid": 27,
            "members": ["luca-cisotto"]
        }
    ]
}
```

## Compatibilità

- **Linux (Ubuntu)**: supportato
- **macOS**: non supportato (mancanza del comando chage e di librerie specifiche per la gestione degli utenti)
