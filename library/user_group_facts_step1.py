from ansible.module_utils.basic import AnsibleModule
import pwd
import grp

def get_users():
    users = {}
    users_by_uid = {}
    for user in pwd.getpwall():
        user_info = {
            "uid": user.pw_uid,
            "gid": user.pw_gid,
            "home": user.pw_dir,
            "shell": user.pw_shell
        }
        users[user.pw_name] = user_info
        users_by_uid[user.pw_uid] = user_info
    return users, users_by_uid

def get_groups():
    groups = {}
    groups_by_gid = {}
    for group in grp.getgrall():
        group_info = {
            "gid": group.gr_gid,
            "members": group.gr_mem
        }
        groups[group.gr_name] = group_info
        groups_by_gid[group.gr_gid] = group_info
    return groups, groups_by_gid

def main():
    module_args = dict(
        include_users=dict(type='bool', required=False, default=True),
        include_groups=dict(type='bool', required=False, default=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    include_users = module.params['include_users']
    include_groups = module.params['include_groups']

    result = {
        "changed": False,
        "ansible_facts": {}
    }

    if include_users:
        users, users_by_uid = get_users()
        result["ansible_facts"]["users"] = users
        result["ansible_facts"]["users_by_uid"] = users_by_uid

    if include_groups:
        groups, groups_by_gid = get_groups()
        result["ansible_facts"]["groups"] = groups
        result["ansible_facts"]["groups_by_gid"] = groups_by_gid

    module.exit_json(**result)

if __name__ == '__main__':
    main()
