#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import pwd
import grp
import subprocess

def get_users():
    users = []
    for p in pwd.getpwall():
        if p.pw_uid >= 1000 and 'nologin' not in p.pw_shell:
            users.append({
                'name': p.pw_name,
                'uid': p.pw_uid,
                'gid': p.pw_gid,
                'home': p.pw_dir,
                'shell': p.pw_shell,
                'expiry': get_password_expiry(p.pw_name)
            })
    return users

def get_groups():
    groups = []
    for g in grp.getgrall():
        groups.append({
            'name': g.gr_name,
            'gid': g.gr_gid,
            'members': g.gr_mem
        })
    return groups

def get_password_expiry(username):
    try:
        output = subprocess.check_output(['chage', '-l', username], text=True)
        for line in output.splitlines():
            if 'Password expires' in line:
                return line.split(':')[1].strip()
    except subprocess.CalledProcessError:
        return 'N/A'
    return 'N/A'

def main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    result = {
        'users': get_users(),
        'groups': get_groups(),
    }
    module.exit_json(changed=False, ansible_facts=result)

if __name__ == '__main__':
    main()
