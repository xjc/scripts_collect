#!/bin/bash

conf_dir='./database.conf'

db_name=[]
index=0
find_location=0
while read line
do
if [[ $line =~ 'global=' ]];then
  #echo $line
  name=${line//[global=/}
  name=${name//]/}
  db_name[$index]=$name
  let "index+=1"
fi
done<$conf_dir

in_conf=0
user=''
password=''
host=''
port=''

if [[ -z $1 ]];then
  echo '目前配置文件中共配置了'$index'个数据库连接信息,分别是:'${db_name[@]}
  echo '=========================如需连接到相应的数据库,请在脚本后面带上数据库名称参数========================='
else
  for item in ${db_name[@]}
  do
    if [[ "$item" = "$1" ]];then
      in_conf=1
      while read line
      do
        until [[ $find_location -eq 1 ]]
        do
          name=${line//[global=/}
          name=${name//]/}
          if [[ "$name" = "$1" ]];then
            find_location=1
          else
            continue 2
          fi
        done

        #echo $line

        if [[ $line =~ "global=" ]];then
          name=${line//[global=/}
          name=${name//]/}
          if [[ $name = $1 ]];then
            continue 
          else
            break
          fi
        fi

        if [[ $line =~ "user=" ]];then
          user=`echo $line | awk -F "=" '{print $2}'`
        elif [[ $line =~ "password=" ]];then
          password=`echo $line | awk -F '=' '{print $2}'`
        elif [[ $line =~ "host=" ]];then
          host=`echo $line | awk -F '=' '{print $2}'`
        elif [[ $line =~ "type=" ]];then
          type=`echo $line | awk -F '=' '{print $2}'`
        elif [[ $line =~ "port=" ]];then
          port=`echo $line | awk -F '=' '{print $2}'`
        fi

      done<$conf_dir
    fi
  done
  if [[ $in_conf -eq 0 ]];then
    echo '数据库名称输入有误, 目前配置文件中共配置了'$index'个数据库连接信息,分别是:'${db_name[@]}
    echo '=========================如需连接到相应的数据库,请在脚本后面带上数据库名称参数========================='
  else
    echo 'user='$user, 'password='$password, 'host='$host, 'type='$type, 'port='$port
    mysql -u$user -p$password -h$host --default-character-set=utf8 
  fi
fi

