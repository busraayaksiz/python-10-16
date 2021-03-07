from datetime import datetime
import locale
print(locale.setlocale(locale.LC_ALL,""))
simdi = datetime.now()#şimdiki zaman
print(simdi)
print(simdi.year)
print(simdi.month)
print(simdi.day)
print(simdi.hour)
print(simdi.second)
print(simdi.minute)
print(simdi.microsecond)
"""------------------------"""
print(simdi.ctime())

print(datetime.strftime(simdi,"%Y"))
print(datetime.strftime(simdi,"%B"))
print(datetime.strftime(simdi,"%A"))
print(datetime.strftime(simdi,"%X"))
print(datetime.strftime(simdi,"%D"))

print(datetime.strftime(simdi, "%Y %B %A"))

"""------------------------------------"""
#timestamp() epoch time
#fromtimestamp() normal zaman convert epoch

print(datetime.timestamp(simdi))
yas = simdi - datetime(1997,1,23)
print(yas.days/365)
