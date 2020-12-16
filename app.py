# Requirements
import subprocess


# Console print initial
print('######################################################################')
print('')
print('########  ##    ##    ########    ###    ########  ##        ##    ##')
print('##     ##  ##  ##          ##    ## ##   ##     ## ##    ##   ##  ##')
print('##     ##   ####          ##    ##   ##  ##     ## ##    ##    ####')
print('########     ##          ##    ##     ## ##     ## ##    ##     ##')
print('##     ##    ##         ##     ######### ##     ## #########    ##')
print('##     ##    ##        ##      ##     ## ##     ##       ##     ##')
print('########     ##       ######## ##     ## ########        ##     ##')
print('')
print('######################################################################')
print('')
# Initial
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':0')[1][1:-1] for line in data if "All User Profile" in line]

print('> Process operating...')
print('> Getting Password.')
print('')
print('Results:')
print('Wi-Fi connection:')

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'Name:{wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name:{wifi}, Password: Cannot be read, try again')
print('')
print('######################################################################')
print('')
print('Close this window to exit.')
print('')

# Metadate
print('Repository: https://github.com/ZAD4YTV/excract-wifi-passwords-from-windows/')
print('BY ZAD4Y')
print('')
print('Title: Extract Wi-Fi passwords from windows.')
print('Description: Extractor of Wi-Fi passwords from windows. I am not responsible for any illegal activities that you perform with the  content of this repository')
print('License: MIT License')
print('More information in the repository.')
