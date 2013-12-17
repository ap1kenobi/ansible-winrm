#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def main():
    tclwinrmrunnerpath = ""
    tclpath = ""
    operationtimeout = "120"

    module = AnsibleModule(
        argument_spec = dict(
            psscriptname=dict(required=True),
            pshostname=dict(required=True),
            psusername=dict(required=True),
            pspassword=dict(required=True),
            tclwinrmrunnerpath=dict(required=False),
            tclpath=dict(required=False),
            operationtimeout=dict(required=False),
        ),
        supports_check_mode=False,
    )

    if not tclwinrmrunnerpath:
        tclwinrmrunnerpath = '/opt/tclwinrunner/winrmrunner.tcl'
    if not tclpath:
        tclpath = '/opt/ActiveTcl-8.6/bin/tclsh'


    psscriptname = module.params['psscriptname']
    pshostname = module.params['pshostname']
    psusername = module.params['psusername']
    pspassword = module.params['pspassword']

    proc = subprocess.Popen([tclpath, tclwinrmrunnerpath, psscriptname,pshostname, psusername, pspassword, operationtimeout], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()

    if err:
            #We have an error
            module.fail_json(msg=err)

    outarray = out.splitlines()

    for line in outarray:
        if "AnsibleResult" in line:
            Ansibleresult = line
            Ansibleresult = Ansibleresult.replace("AnsibleResult:","")
        if "AnsibleDetail" in line:
            AnsibleDetail = line
            AnsibleDetail = AnsibleDetail.replace("AnsibleDetail:","")
        if "AnsibleError" in line:
            AnsibleError = line
            AnsibleError = AnsibleError.replace("AnsibleError:","")
    
    if AnsibleError:
            #We have a script-based error
            module.fail_json(msg="Script-based error: " + AnsibleError)

    #No error
    if Ansibleresult == "Changed":
        changed=True
    elif Ansibleresult == "Unchanged":
        changed=False
    else:
        changed=True

    module.exit_json(changed=changed,msg=AnsibleDetail)




# import module snippets
from ansible.module_utils.basic import *
main()
