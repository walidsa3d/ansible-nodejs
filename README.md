Ansible-NodeJS
=========
An Ansible role to install nodejs on Ubuntu.
![Ansible Role](https://img.shields.io/ansible/role/d/walidsa3d/nodejs)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/walidsa3d/ansible-nodejs/main.yml)

Install
------------
```
ansible-galaxy role install walidsa3d.nodejs

```

Requirements
------------

- None

Variables
--------------
```yaml
nodej_version: "21"
```

Dependencies
------------
- None

Example Playbook
----------------
```yaml
- hosts: all
  roles:
    - walidsa3.nodejs
```
License
-------

MIT
