import subprocess

PSSCRIPTFILE = '/home/trond/Documents/ansible-winrm/script.ps1'
PSHOSTNAME = "192.168.188.155"
PSUSERNAME = "Administrator"
PSPASSWORD = "MyPassword"
proc = subprocess.Popen(['/opt/ActiveTcl-8.6/bin/tclsh', '/home/trond/Documents/ansible-winrm/winrmrunner.tcl', PSSCRIPTFILE,PSHOSTNAME, PSUSERNAME, PSPASSWORD], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = proc.communicate()
#outtext = out.rstrip()
#outtext = outtext.strip()

#print 'stdout:', outtext

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
    print "An error ocurred"
if AnsibleError:
    print "A script-error ocurred: " + AnsibleError

#RESULT = "Fake"
#print RESULT

if Ansibleresult == 'Changed':
    print 'Changed stuff'
elif Ansibleresult == 'Unchanged':
    print 'Did not change stuff'
else:
    print "Not sure what we did"
print AnsibleDetail


#tcl = Tcl()
# Execute proc main from foo.tcl with MYFILE as the arg
#tcl.eval('source /home/trond/Documents/ansible-py/winrmrunner.tcl')
#tcl_str = tcl.eval('main %s' % MYFILE)


# Access the contents of a Tcl variable, $tclVar from python
#tcl.eval('set tclVar foobarme')
#tclVar = tcl.eval('return $tclVar')
