# 1 安装插件

![image-20190521224110981](/Users/xiaorui/Library/Application Support/typora-user-images/image-20190521224110981.png)

`robotframework`插件

`Multijob`插件

`Node and Label parameter plugin`插件



# 2 新建流水线任务



![image-20190521224431978](/Users/xiaorui/Library/Application Support/typora-user-images/image-20190521224431978.png)



添加脚本

![image-20190521224617476](/Users/xiaorui/Library/Application Support/typora-user-images/image-20190521224617476.png)

```groovy
//nodeName请填写node的IP地址
nodeName='master'
//stages请增加需要的步骤
def stages = ['Function_ifconfig']
node(nodeName){
echo"Triggering on"+nodeName 
for(int i=0;i<stages.size();++i){
    stage(stages[i]){
    build job:stages[i],parameters:[
    new org.jvnet.jenkins.plugins.nodelabelparameter.NodeParameterValue("TARGET_NODE","description",nodeName)]
    }
  }
} 
```

# 3 创建任务

![image-20190521233848676](/Users/xiaorui/Library/Application Support/typora-user-images/image-20190521233848676.png)

选择执行shell

![image-20190521234047863](/Users/xiaorui/Library/Application Support/typora-user-images/image-20190521234047863.png)

编写Pipeline_master调用Function_ifconfig2

![image-20190521234232439](/Users/xiaorui/Library/Application Support/typora-user-images/image-20190521234232439.png)



立即构建任务

