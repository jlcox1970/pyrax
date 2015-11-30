#!/bin/bash
csv="/tmp/server_costs.csv"
cmd="python list_servers.py 2>/dev/null"
srv_txt=`$cmd 2>/dev/null `
#srv=`$cmd 2>/dev/null |grep Name |cut -d: -f2 |sed 's/ //g'`
echo "Name,Flavor,Cost/h">$csv
srv=`echo $srv_txt |sed 's/Name/\nName/g'`
cost_hour="0"
IFS='	
'
for i in $srv
do
	IFS=` 	
	`
	name=`echo $i|awk '{print $2}'`
	flavor=`echo $i  |cut -d\' -f4 `
	cost=`cat server.price |grep ^${flavor}= |cut -d= -f2 |cut -d, -f1`
	echo   $name,$flavor,$cost >>$csv
	cost_hour=`echo "scale=2; $cost_hour + $cost" |bc -l`
done

echo "0 rackspace cost_hour=$cost_hour Cost per Hour is $cost_hour"
exit
echo Hourly Cost::: $cost_hour

exit
python list_servers.py  |grep Flavor |cut -d\' -f4 |grep [a-z]

