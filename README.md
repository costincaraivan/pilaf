
# shepy

Utility methods to make file and process operations a bit closer to shell scripts

# Commands

| Busybox command | Shepy equivalent | Category |
| --------------- | ---------------- | -------- |
| \[, \[\[, false, sleep, test, timeout, true, usleep, watch, xargs, yes | N/A | Flow control |
| acpid, beep, brctl, eject, sync, sysctl, taskset, vcontrol, volname, zcip | N/A | Hardware control |
| addgroup | addgroup | User interaction |
| adduser | adduser | User integration |
| adjtimex | |
| ar, bunzip2, bzcat, bzip2, cpio, gunzip, tar, uncompress, unexpand, unlzma, unlzop, unzip, zcat | archive | Archivers |
| arp, arping | N/A | Network |
| awk | N/A | Scripting tools |
| basename | basename | Filesystem interaction |
| blkid | |
| cal | |
| ash, catv, clear, less, more, sh, telnetd, tftpd, top, tty, ttysize, uname, uptime, vlock | N/A | Interactivity |
| chat | |
| chattr |
| chgrp |  |
| chmod |  |
| chown |  |
| chpasswd |  |
| chpst |  |
| chroot |  |
| chrt |  |
| chvt |  |
| cksum |  |
| cmp |  |
| comm |  |
| cp | cp | Filesystem interaction |
| crond |  |
| crontab |  |
| cryptpw |  |
| cut |  |
| date |  |
| dc |  |
| dd |  |
| deallocvt |  |
| delgroup |  |
| deluser |  |
| depmod |  |
| devmem |  |
| df |  |
| dhcprelay |  |
| diff |  |
| dirname |  |
| dmesg |  |
| dnsd |  |
| dnsdomainname |  |
| dos2unix |  |
| dpkg | N/A |
| du |  |
| dumpkmap |  |
| dumpleases |  |
| cat, echo, ed, printf, sed, head, tac, tail, tee, tr, vi, uniq, watchdog, wc | N/A | Printing/editing |
| egrep |  |
| env |  |
| envdir |  |
| envuidgid |  |
| expand |  |
| expr |  |
| fakeidentd |  |
| fbset |  |
| fbsplash |  |
| fdflush |  |
| fdformat |  |
| fdisk |  |
| fgrep |  |
| find |  |
| findfs |  |
| flash_lock |  |
| flash_unlock |  |
| fold |  |
| free |  |
| freeramdisk |  |
| fsck |  |
| fsck.minix |  |
| fsync |  |
| ftpd |  |
| ftpget |  |
| ftpput |  |
| fuser |  |
| getopt |  |
| getty |  |
| grep |  |
| hd |  |
| hdparm |  |
| hexdump |  |
| hostid |  |
| hostname |  |
| httpd |  |
| hush |  |
| hwclock |  |
| id |  |
| ifconfig |  |
| ifdown |  |
| ifenslave |  |
| ifplugd |  |
| ifup |  |
| inetd |  |
| init |  |
| inotifyd |  |
| insmod |  |
| install |  |
| ionice |  |
| ip |  |
| ipaddr |  |
| ipcalc |  |
| ipcrm |  |
| ipcs |  |
| iplink |  |
| iproute |  |
| iprule |  |
| iptunnel |  |
| kbd_mode |  |
| kill |  |
| killall |  |
| killall5 |  |
| klogd |  |
| last |  |
| length |  |
| linux32, linux64, linuxrc | N/A | Misc |
| ln |  |
| loadfont |  |
| loadkmap |  |
| logger |  |
| login |  |
| logname |  |
| logread |  |
| losetup |  |
| lpd |  |
| lpq |  |
| lpr |  |
| ls |  |
| lsattr |  |
| lsmod |  |
| lzmacat |  |
| lzop |  |
| lzopcat |  |
| makemime |  |
| man |  |
| md5sum |  |
| mdev |  |
| mesg |  |
| microcom |  |
| mkdir |  |
| mkdosfs |  |
| mkfifo |  |
| mkfs.minix |  |
| mkfs.vfat |  |
| mknod |  |
| mkpasswd |  |
| mkswap |  |
| mktemp |  |
| modprobe |  |
| mount |  |
| mountpoint |  |
| mt |  |
| mv | mv | Filesystem interaction |
| nameif |  |
| nc |  |
| netstat |  |
| nice |  |
| nmeter |  |
| nohup |  |
| nslookup |  |
| od |  |
| openvt |  |
| passwd |  |
| patch |  |
| pgrep |  |
| pidof |  |
| ping |  |
| ping6 |  |
| pipe_progress |  |
| pivot_root |  |
| pkill |  |
| popmaildir |  |
| printenv |  |
| ps |  |
| pscan |  |
| pwd |  |
| raidautorun |  |
| rdate |  |
| rdev |  |
| readlink |  |
| readprofile |  |
| realpath |  |
| reformime |  |
| renice |  |
| reset |  |
| resize |  |
| rm, rmdir | rm | Filesystem interaction |
| rmmod |  |
| route |  |
| rpm |  |
| rpm2cpio |  |
| rtcwake |  |
| run-parts |  |
| runlevel |  |
| runsv |  |
| runsvdir |  |
| rx |  |
| script |  |
| scriptreplay |  |
| sendmail |  |
| seq |  |
| setarch |  |
| setconsole |  |
| setfont |  |
| setkeycodes |  |
| setlogcons |  |
| setsid |  |
| setuidgid |  |
| sha1sum |  |
| sha256sum |  |
| sha512sum |  |
| showkey |  |
| slattach |  |
| softlimit |  |
| sort |  |
| split |  |
| start-stop-daemon |  |
| stat |  |
| strings |  |
| stty |  |
| su |  |
| sulogin |  |
| sum |  |
| sv |  |
| svlogd |  |
| swapoff |  |
| swapon |  |
| switch_root |  |
| syslogd | ? | ? |
| time |  |
| touch | open | Filesystem interaction |
| traceroute | N/A | Network |
| udhcpc, udhcpd | N/A | Network |
| udpsvd, tcpsvd | N/A | Network |
| umount | ? | Filesystem interaction |
| unix2dos | unix2dos | Conversions |
| uudecode | uudecode | Conversions |
| uuencode | uuencode | Conversions |
| telnet, tftp, wget | curl | Network |
| which | which | System info |
| who | who | System info |
| whoami | whoami | System info |