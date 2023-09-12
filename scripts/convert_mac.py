import re 

class MacFormatting:

    def __init__(self, mac):
        self.mac = mac

    @staticmethod
    def _validate_delimiter(delimiter):
        """
        Takes delimiter as string parameter or None
        Verify delimiter is an acceptable option.
        If valid returns True, otherwise False
        """

        if delimiter in ['.', ':', '-', None]:
            return delimiter

        return False

    @staticmethod
    def _validate_step(step):
        """
        Take step as parameter.
        If necessary, convert step to integer.
        If valid return step as int, otherwise return None.
        """

        if isinstance(step, str):
            if step.isnumeric():
                step = int(step)

        if step in [0, 2, 4]:
            return step

        return None

    def strip_formatting(self):
        """
        Takes a MAC address as string parameter.
        Strips away formatting, and performs validation.
        If valid, returns stripped MAC address, otherwise returns None
        """

        mac_address = self.mac.strip().lower()

        if not re.search(r'[g-z]', mac_address):
            mac_address = ''.join(re.split(r'\W', mac_address))
            if len(mac_address) == 12:
                return mac_address

        return None

    def reformat(self, delimiter, step):

        mac = self.strip_formatting()
        delimiter = self._validate_delimiter(delimiter)
        step = self._validate_step(step)

        if mac and step is not None:
            if delimiter:
                return mac if step == 0 else str(delimiter).join(mac[i:i + step] for i in range(0, 12, step))
            else:
                return mac

        return None


if __name__ == "__main__":
    # Executed when file is run directly
    # python3 /home/runner/Notebook/scripts/convert_mac.py
    
    mac_address_list = ['00:1b:63:84:45:e6', '00-1B-63-84-45-E6',
                        '001B638445E6', '00.1b.63.84.45.e6',
                        '001b.6384.45e6', 'aa.bb.cc.dd.ee.fh']

    counter = 0
    for mac in mac_address_list:
        print(f'MAC #{counter}: {mac}')
        arista_mac = MacFormatting(mac)
        print('Test 1:', arista_mac.reformat('-', '4'))
        print('Test 2:', arista_mac.reformat('.', 4))
        print('Test 3:', arista_mac.reformat('.', None))
        print('Test 4:', arista_mac.reformat(None, None))
        print('Test 5:', arista_mac.reformat('#', None))
        print('Test 6:', arista_mac.strip_formatting())
        print('~~~~~~~~~~~~~~~~~~~~~~~~\m')
        counter += 1

else:
    # Code executed when file is imported
   print("File one executed when imported")


