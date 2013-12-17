import subprocess

PSSCRIPTFILE = 'script.ps1'
PSHOSTNAME = "192.168.188.155"
PSUSERNAME = "Administrator"
PSPASSWORD = "MyPassword123"
timeout = "500"
proc = subprocess.Popen(['/opt/ActiveTcl-8.6/bin/tclsh', 'winrmrunner.tcl', PSSCRIPTFILE,PSHOSTNAME, PSUSERNAME, PSPASSWORD], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = proc.communicate()
#outtext = out.rstrip()
#outtext = outtext.strip()

#print 'stdout:', outtext

if err:
    print "An error ocurred"

outarray = out.splitlines()

AnsibleError = None
Ansibleresult = None
AnsibleDetail = None

for line in outarray:
    if "AnsibleResult" in line:
        Ansibleresult = line
        Ansibleresult = Ansibleresult.replace("Ansibleresult:","")
    if "AnsibleDetail" in line:
        AnsibleDetail = line
        AnsibleDetail = AnsibleDetail.replace("AnsibleDetail:","")
    if "AnsibleError" in line:
        AnsibleError = line
        AnsibleError = AnsibleError.replace("AnsibleError:","")

if AnsibleError:
    print "A script-error ocurred: " + AnsibleError


if Ansibleresult == 'Changed':
    print 'Changed stuff'
elif Ansibleresult == 'Unchanged':
    print 'Did not change stuff'
else:
    print "Not sure what we did"
print AnsibleDetail


