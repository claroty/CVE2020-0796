
# CVE2020-0796

For more information see in https://blog.claroty.com/advisory-new-wormable-vulnerability-in-microsoft-smbv3

## SMBv3 Compression Tester
Multiple scripts and detection tools to check if a Windows machine has SMBv3 protocol enabled with the compression feature. 
* NSE script
* Python script
* Snort rules alerting on compressed SMB traffic, and compression-enabled hosts

## Notes
Our NSE script is based on `smb2-capabilities.nse` which we expanded to detect SMBv3 compression as well. Currently it's a standalone NSE script with a patched lua file but we will PR the nmap repository with those changes.

## Example

    Starting Nmap 7.80SVN ( https://nmap.org ) at 2020-03-11 18:17 IST
    Nmap scan report for 1.2.3.4
    Host is up (0.00050s latency).
    
    PORT    STATE SERVICE
    445/tcp open  microsoft-ds
    
    Host script results:
    | smb2-capabilities_patched:
    |   2.02:
    |     Distributed File System
    |   2.10:
    |     Distributed File System
    |     Leasing
    |     Multi-credit operations
    |   3.00:
    |     Distributed File System
    |     Leasing
    |     Multi-credit operations
    |   3.02:
    |     Distributed File System
    |     Leasing
    |     Multi-credit operations
    |   3.11:
    |     Distributed File System
    |     Leasing
    |     Multi-credit operations
    |_    SMBv3 Compression LZTN1 (Negotiation Context)   <----------

## Supported CVEs

* CVE2020-0796

## Requirements

* nmap

## Usage
`cd` into run `SMBv3Compression` (your cwd must be the same as the files) and run:

    nmap -p445 --script ./smb2-capabilities_patched.nse IP_ADDR

Search for `SMBv3 Compression LZTN1 (Negotiation Context)`.


## Disable SMBv3 compression
You can disable SMBv3 compression with the PowerShell command below:

    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" DisableCompression -Type DWORD -Value 1 -Force

## License
Apache License 2.0. See the parent directory.


## Disclaimer
There is no warranty, expressed or implied, associated with this product.
