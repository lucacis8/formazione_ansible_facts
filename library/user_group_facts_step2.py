from ansible.module_utils.basic import AnsibleModule
import csv

def parse_passwd():
    """ Legge il file /etc/passwd e restituisce un dizionario con informazioni sugli utenti. """
    users = {}
    with open('/etc/passwd', 'r') as passwd_file:
        reader = csv.reader(passwd_file, delimiter=':')
        for row in reader:
            if len(row) == 7:  # Assicurati che ogni riga abbia esattamente 7 colonne
                username, password, uid, gid, gecos, home, shell = row
                users[username] = {
                    'uid': int(uid),
                    'gid': int(gid),
                    'gecos': gecos,
                    'home': home,
                    'shell': shell
                }
            else:
                # Se la riga non ha il numero corretto di colonne, la ignoriamo
                continue
    return users

def parse_group():
    """ Legge il file /etc/group e restituisce un dizionario con informazioni sui gruppi. """
    groups = {}
    with open('/etc/group', 'r') as group_file:
        reader = csv.reader(group_file, delimiter=':')
        for row in reader:
            if len(row) == 4:  # Verifica che la riga abbia esattamente 4 colonne
                group_name, password, gid, members = row
                groups[group_name] = {
                    'gid': int(gid),
                    'members': members.split(',') if members else []
                }
            else:
                # Se la riga non ha il numero corretto di colonne, la ignoriamo
                continue
    return groups

def enrich_user_data(users, groups):
    """ Arricchisce i dati degli utenti con il nome del gruppo principale e i gruppi aggiuntivi. """
    for username, user_info in users.items():
        user_gid = user_info['gid']
        for group_name, group_info in groups.items():
            if group_info['gid'] == user_gid:
                user_info['primary_group'] = group_name
                break
        user_info['additional_groups'] = [group_name for group_name, group_info in groups.items() if username in group_info['members']]
    return users

def main():
    module_args = dict(
        gather_users=dict(type='bool', required=False, default=True),
        gather_groups=dict(type='bool', required=False, default=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    try:
        users = {}
        groups = {}

        if module.params['gather_users']:
            users = parse_passwd()

        if module.params['gather_groups']:
            groups = parse_group()

        # Arricchisci i dati utente con i gruppi
        users = enrich_user_data(users, groups)

        module.exit_json(
            changed=False,
            ansible_facts=dict(users=users, users_by_uid={user['uid']: user for user in users.values()})
        )

    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()
