#!/usr/bin/python
from lxml import html
import requests

# Get the EFI/SMC table from Apple's Website
page = requests.get('http://support.apple.com/en-us/HT1237')
tree = html.fromstring(page.text)

# Count the number of rows which will be used in looping
rows = tree.xpath('//*[@id="kbtable"]/tbody/tr')

# For each row:
for i in range(len(rows)):
	# Get the friendly name, model, EFI version, SMC version, and the download URLs
	friendly_name = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[1]/text()' % locals())
	model = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[2]/p/text()' % locals())
	efi_version = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[3]/p/a/text()' % locals())
	efi_url = tree.xpath('//*[@id="kbtable"]/tbody/tr[3]/td[3]/p/a/@href' % locals())
	smc_version = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[4]/p/a/text()' % locals())
	smc_url = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[4]/a/@href' % locals())
	
	# Print everything in a human-readable format
	if not friendly_name:
		continue
	else:
		print friendly_name[0]
		
	if not model:
		model = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[2]/text()' % locals())
		print model[0]
	else:
		print model[0]
		
	if not efi_version:
		efi_version = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[3]/a/text()' % locals())
		if not efi_version:
			print 'No EFI'
		else:
			print efi_version[0]
			print efi_url[0]
	else:
		print efi_version[0]
		
	if not smc_version:
		smc_version = tree.xpath('//*[@id="kbtable"]/tbody/tr[%(i)s]/td[4]/a/text()' % locals())
		if not smc_version:
			print 'No SMC'
		else:
			print smc_version[0]
			print smc_url[0]
	else:
		print smc_version[0]
	print '\n'
