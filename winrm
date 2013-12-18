#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def main():
    tclwinrmrunnerpath = ""
    tclpath = ""
    operationtimeout = ""
    debugmode = ""

    module = AnsibleModule(
        argument_spec = dict(
            psscriptname=dict(required=True),
            pshostname=dict(required=True),
            psusername=dict(required=True),
            pspassword=dict(required=True),
            tclwinrmrunnerpath=dict(required=False),
            tclpath=dict(required=False),
            operationtimeout=dict(required=False),
            debugmode=dict(required=False),
        ),
        supports_check_mode=False,
    )

    if not tclwinrmrunnerpath:
        tclwinrmrunnerpath = '/opt/tclwinrunner/winrmrunner.tcl'
    if not tclpath:
        tclpath = '/opt/ActiveTcl-8.6/bin/tclsh'
    if not operationtimeout:
        operationtimeout = '120'
    if not debugmode:
        debugmode = '0'


    psscriptname = module.params['psscriptname']
    pshostname = module.params['pshostname']
    psusername = module.params['psusername']
    pspassword = module.params['pspassword']
    operationtimeout = module.params['operationtimeout']
    debugmode = module.params['debugmode']

    proc = subprocess.Popen([tclpath, tclwinrmrunnerpath, psscriptname,pshostname, psusername, pspassword], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()

    if err:
            #We have an error
            module.fail_json(msg=err)

    outarray = out.splitlines()

    AnsibleError = None
    AnsibleResult = None
    AnsibleDetail = None

    for line in outarray:
        if "AnsibleResult" in line:
            AnsibleResult = line
            AnsibleResult = AnsibleResult.replace("AnsibleResult:","")
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
    if AnsibleResult == "Changed":
        changed=True
    elif AnsibleResult == "Unchanged":
        changed=False
    else:
        changed=True

    module.exit_json(changed=changed,msg=out)

# import module snippets
from ansible.module_utils.basic import *
main()
