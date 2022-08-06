#!/bin/bash
# 获取镜像名参数
if [[ ${#} < 2 ]] ; then
	printf "\e[1;31m=======>脚本请求参数不符合规范，本次运行终止！！！ \e[0m \n"
	printf "\e[1;32m=======>调用格式：sh import_docker_image.sh twise-5g-ccc 9781   \e[0m \n"
	exit 1
fi
image_name=${1}
run_port=${2}
printf "\e[1;32m=======>镜像名称:[${image_name}]。 \e[0m \n"
image_full_file_name=$(ls ${image_name}-*.tar)

image_version=V$(echo ${image_full_file_name} | grep -Po "(?<=-V).*?(?=\.tar)")

printf "\e[1;32m=======>镜像版本:[${image_version}]。 \e[0m \n"
docker stop ${image_name}
docker rm ${image_name}

printf "\e[1;32m=======>镜像名称:[${image_name}]。 \e[0m \n"
old_image_version=$(docker images 192.169.2.237:8004/5g-platform-test/${image_name} --format "{{.Tag}} {{.CreatedAt}}" | sort -rk 2 | awk 'NR==1{print $1}')
printf "\e[1;32m=======>旧镜像版本:[${old_image_version}]。 \e[0m \n"
if [[ -z "${old_image_version}" ]] ; then
    docker rmi 192.169.2.237:8004/5g-platform-test/${image_name}:${old_image_version}
fi
docker load -i ${image_full_file_name}

java_opts='1'
if [[ "${image_name}" == "5g-aim-editor" ]] ; then
    JAVA_OPTS='-Xmn2G -Xms4G -Xmx5G -XX:SurvivorRatio=8'
fi

printf "\e[1;32m=======>JAVA_OPTS:[${java_opts}]。 \e[0m \n"
printf "\e[1;32m=======>启动docker程序:[${image_name}:${image_version}]。 \e[0m \n"
docker run --init -d --net=host --name ${image_name} \
-p ${run_port}:${run_port} \
-v /opt/java/logs/${image_name}:/opt/java/logs/${image_name} -v /opt/java/${image_name}/config:/opt/java/${image_name}/config \
-v /opt/java/${image_name}/mon_data:/opt/java/${image_name}/mon_data -v /opt/java/${image_name}/file:/opt/java/${image_name}/file \
-e "SPRING_PROFILES_ACTIVE=prod"  \
-e "JAVA_OPTS='${java_opts}'" \
192.169.2.237:8004/5g-platform-test/${image_name}:${image_version}

