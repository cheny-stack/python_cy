#!/bin/bash
# 获取镜像名参数
if [[ ${#} < 1 ]] ; then
	printf "\e[1;31m=======>脚本请求参数不符合规范，本次运行终止！！！ \e[0m \n"
	printf "\e[1;32m=======>调用格式：sh export_docker_image.sh twise-5g-ccc  \e[0m \n"
	exit 1
fi
image_name=${1}
printf "\e[1;32m=======>镜像名称:[${image_name}]。 \e[0m \n"
image_version=$(docker images 192.169.2.237:8004/5g-platform-test/${image_name} --format "{{.Tag}} {{.CreatedAt}}" | sort -rk 2 | awk 'NR==1{print $1}')
printf "\e[1;32m=======>镜像版本:[${image_version}]。 \e[0m \n"
# 导出镜像文件
docker save -o ${image_name}-${image_version}.tar 192.169.2.237:8004/5g-platform-test/${image_name}:${image_version}