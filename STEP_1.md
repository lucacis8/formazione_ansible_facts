# Formazione Ansible Facts

## Descrizione
Questo progetto ha lo scopo di introdurre l'uso dei **moduli personalizzati di Ansible** per raccogliere e popolare gli **Ansible Facts** con informazioni sugli utenti e sui gruppi di sistema.

Lo **Step 1** prevede la creazione di un modulo che:
- Colleziona informazioni sugli utenti presenti nel sistema.
- Colleziona informazioni sui gruppi.
- Popola gli Ansible Facts con questi dati in due strutture:
  - `ansible_facts['users']`: Dizionario con gli username come chiavi.
  - `ansible_facts['users_by_uid']`: Dizionario con gli UID come chiavi.
  - `ansible_facts['groups']`: Dizionario con i nomi dei gruppi.
  - `ansible_facts['groups_by_gid']`: Dizionario con i GID.

## Struttura del Progetto

```bash
formazione_ansible_facts/ 
├── library/ 
│ └── user_group_facts.py # Modulo Ansible personalizzato 
├── test_playbook.yml # Playbook per testare il modulo 
└── STEP_1.md # Documentazione del progetto
```

## Requisiti

- **Python** ≥ 3.8 (Consigliato Python 3.13.1)  
- **Ansible** ≥ 2.10 (Verificato con Ansible Core 2.18.1)  

### Installazione di Ansible
Se Ansible non è installato, eseguire:

```bash
pip install ansible
```

## Esecuzione

1. Clonare la repository (se necessario) ed entrare nella directory:
```bash
cd formazione_ansible_facts
```

2. Eseguire il playbook:
```bash
ansible-playbook -i localhost, test_playbook.yml
```

3. Output atteso:
I facts personalizzati verranno mostrati, ad esempio:
```yaml
"ansible_facts": {
    "users": {
        "root": {
            "uid": 0,
            "gid": 0,
            "home": "/root",
            "shell": "/bin/bash"
        },
        "lucacisotto": {
            "uid": 501,
            "gid": 20,
            "home": "/Users/lucacisotto",
            "shell": "/bin/zsh"
        }
    },
    "users_by_uid": {
        "0": {
            "uid": 0,
            "gid": 0,
            "home": "/root",
            "shell": "/bin/bash"
        },
        "501": {
            "uid": 501,
            "gid": 20,
            "home": "/Users/lucacisotto",
            "shell": "/bin/zsh"
        }
    },
    "groups": {
        "staff": {
            "gid": 20,
            "members": ["lucacisotto"]
        }
    },
    "groups_by_gid": {
        "20": {
            "gid": 20,
            "members": ["lucacisotto"]
        }
    }
}
```

## Possibili Errori

- **Errore di SSH:**
Se si riceve un errore come:
```vbnet
ssh: connect to host localhost port 22: Connection refused
```
Aggiungere questa riga al playbook:
```yaml
connection: local
```

## Riferimenti

- Ansible Plugins
- Guida alla creazione di moduli Ansible
