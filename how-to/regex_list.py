# Useful Link: https://regex101.com/
# Documnetation = https://docs.python.org/3.4/howto/regex.html
# https://www.tutorialspoint.com/python/python_reg_expressions.htm


#############################################
# Using re module
#############################################
import re
re.findall("regex", "string") # - Find all occurances of 'regex' in the 'string'
re.search("regex", "string") # - Finds first occurance of 'regex' in 'string'
re.match("regex", "string") # - Finds occurange of 'regex' in beggining of 'string'


#############################################
# Cisco Regex
#############################################
regex_IOS = r"^\b(Cisco IOS [Ss]oftware)\b"
regex_IOS_XE = r"^\b(Cisco IOS[-\s]XE [Ss]oftware)\b"
regex_IOS_XR = r"^\b(Cisco IOS[-\s]XR [Ss]oftware)\b"
regex_NX_OS = r"^\b(Cisco Nexus Operating System \(NX[-\s]OS\) [Ss]oftware)\b"
regex_ASA = r"\b(Cisco Adaptive Security Appliance [Ss]oftware)\b"

regex_IP = r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"
regex_MAC = r"\b(?:[0-9a-fA-F]\.?){12}\b"
regex_InterfaceName = r"([Ee]th|[Gg]ig|[Gg]i|[Tt]e|[Tt]w|[Vv]l|[Pp]o|[Vv]lan|[Ll]o|[Ff]o|[Tt]we|[Ee]thernet|[Ff]ast[Ee]thernet|[Gg]igabit[Ee]thernet|[Pp]ort-channel|[Tt]wo[Gg]igabit[Ee]thernet|[Tt]en[Gg]igabit[Ee]thernet|[Ff]orty[Gg]igabit[Ee]thernet|[Tt]wenty[Ff]ive[Gg]ig[Ee])\s?(\d{1,4}(?:\/\d{0,4}){0,2})"
regex_OSPF = r"\b(router ospf \d{1,5})\b"
regex_EIGRP = r"\b(router eigrp \d{1,5})\b"
regex_BGP = r"\b(router bgp \d{1,5})\b"

regex_InterfaceParent = r"^\b(?:(?:interface\s{1})(?:Eth|Gig|Vlan|Po|Lo|FastEthernet|GigabitEthernet|Loopback|Port-channel)\s?\d{1,3}(?:/\d{0,3}){0,2})\b"
regex_Parent_OSPF = r"^\b(router ospf \d{1,5})\b"
regex_Parent_EIGRP = r"^\b(router eigrp \d{1,5})\b"
regex_Parent_BGP = r"^\b(router bgp \d{1,5})\b"
regex_Parent_Keyword = r"(^{0}|^(?!banner)^\w.*{0}.*)"
regex_Child_Keyword = r"(^\s.*{0}.*)"

regex_cdp_hostname = r"(Device ID:)(.*)\b"
regex_cdp_interface = r"(Interface:)\s((?:Eth|Gig|Gi|Te|Tw|Vl|Po|Vlan|Lo|Fo|Twe|Ethernet|FastEthernet|GigabitEthernet|Port-channel|TwoGigabitEthernet|TenGigabitEthernet|FortyGigabitEthernet|TwentyFiveGigE)\s?(\d{1,4}(?:\/\d{0,4}){0,2}))"

regex_ios_acl_parent = r"(Standard IP access list|Extended IP access list) (\S+)"
regex_ios_ace_child = r"(\d+ (permit|deny))"
regex_nxos_acl_parent = r"(IPV4 ACL) (\S+)"
regex_nxos_ace_child = r"(\d+ (permit|deny|remark))"
regex_asa_acl = r"access-list\s(\S+)\sline\s(\d+)\s"
regex_asa_acl_hitcount = r".*(\(hitcnt=\d+\)\s0x[\d\w]+)"

#############################################
# Ubuntu Regex
#############################################
regex_ubuntu_ping = r"\b(?:\d+ bytes from .* icmp_seq=\d ttl=\d+ time=.* ms)\b"

#############################################
# Time Regex
#############################################
# Format 9:26:08 AM
regex_time_a = r"(?:\d{1,2}:[0-5][0-9]:[0-5][0-9]\s[AP]M)"
