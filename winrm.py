#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def main():
    module = AnsibleModule(
        argument_spec = dict(
            psscriptname=dict(required=True),
            pshostname=dict(required=True),
            psusername=dict(required=True),
            pspassword=dict(required=True),
        ),
        supports_check_mode=False,
    )

    psscriptname = module.params['psscriptname']
    pshostname = module.params['pshostname']
    psusername = module.params['psusername']
    pspassword = module.params['pspassword']

    proc = subprocess.Popen(['/opt/ActiveTcl-8.6/bin/tclsh', '/home/trond/Documents/ansible-winrm/winrmrunner.tcl', psscriptname,pshostname, psusername, pspassword], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()

    outarray = out.splitlines()

    for line in outarray:
        if "AnsibleResult" in line:
            Ansibleresult = line
        if "AnsibleDetail" in line:
                AnsibleDetail = line
        if "AnsibleError" in line:
            AnsibleError = line

    Ansibleresult = Ansibleresult.replace("Ansibleresult:","")
    AnsibleDetail = AnsibleDetail.replace("AnsibleDetail:","")
    AnsibleError = AnsibleError.replace("AnsibleError:","")


    if err:
            #We have an error
            module.fail_json(msg=err)
    elif AnsibleError:
            #We have a script-based error
            module.fail_json(msg="Script-based error: " + AnsibleError)

    else:
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
