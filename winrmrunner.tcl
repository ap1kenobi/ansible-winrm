#lappend auto_path /opt/ActiveTcl-8.6/lib
#lappend auto_path /opt/ActiveTcl-8.6/lib/tcl8.6
#lappend auto_path /opt/ActiveTcl-8.6/lib/teapot/package/linux-glibc2.3-x86_64/lib
#lappend auto_path /opt/ActiveTcl-8.6/lib/teapot/package/tcl/lib
#lappend auto_path ../

#puts $auto_path


package require tclwinrm
package require base64

set psscriptpath  [lindex $argv 0]
#puts $psscriptpath

set winrmhostname [lindex $argv 1]
#puts $winrmhostname

set winrmusername [lindex $argv 2]
#puts $winrmusername

set winrmpassword [lindex $argv 3]
#puts $winrmpassword

set operationtimeout [lindex $argv 4]

set address $winrmhostname
set port 5985
set user $winrmusername
set pass $winrmpassword


tclwinrm::configure http $address $port $user $pass
set fp [open $psscriptpath r]
     set script [read $fp]
     close $fp

#set script {$strComputer = $Host
#	$RAM = WmiObject Win32_ComputerSystem
#	$MB = 1048576
#	"Installed Memory: " + [int]($RAM.TotalPhysicalMemory /$MB) + " MB"
#}
set command "powershell -encodedcommand [::base64::encode -wrapchar "" [encoding convertto unicode $script]]"
set result [tclwinrm::rshell $command 120 0]
puts \n$result



