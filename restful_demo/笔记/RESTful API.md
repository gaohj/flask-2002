# RESTful API  

> api  俗称接口   前后端分离 使用的就是 api进行 交互    



## restful  风格 

> 风格  不是标准    

### 协议 

1. http 
2. https 

### 数据传输格式  

 `json` 不用 xml  



### url 链接 

1. 只能是名词  不能是动词   名词的复数 + s   

   比如我要获取博客园下面所有的博客  https://cnblogs.com/api/blogs/

   不能写成  https://cnblogs.com/api/get_blog/

2. 可以用  http://api.blogs.com/blogs/

   也可以用http://www.blogs.com/api/blogs/

### 请求方法  

* GET       等同于  select 
* POST   等同于  insert  
* PUT         等同于 update    全量更新  
* PATCH   等同于 update    增量更新 
* DELETE  等同于 delete   删除   

#### 实例 

* GET  http://api.baidu.com/users/  #查询所有的用户 
* GET http://api.baidu.com/user/id/  #查询指定的用户  
* POST http://api.baidu.com/user   #增加一个用户  
* PATCH    http://api.baidu.com/user/id  #增量更新 修改指定用户的信息 只需要提交修改的字段信息即可 
* PUT  http://api.baidu.com/user/id #全量更新   需要提交所有的字段的信息   
* DELETE  http://api.baidu.com/user/id #删除指定的 用户  



### 状态码   

| 状态码 | 说明                                                     |
| ------ | -------------------------------------------------------- |
| 200    | 服务器成功响应了客户端的请求                             |
| 400    | 用户发送的请求有错误 服务器并没有进行 添加或者修改的操作 |
| 401    | 用户没有权限访问                                         |
| 403    | 因为 某些原因禁止访问                                    |
| 404    | 请求的地址不存在                                         |
| 405    | 请求方法有错误  比如只允许  GET 请求  你发送的POST       |
| 406    | 用户的请求 不被服务器接收                                |
| 500    | 服务器内部的错误  一般是你的代码出bug了                  |
| 502    | A服务依赖于B服务运行 但是 B服务出现了故障  那么 报502    |





## 全国天气预报接口  



| Author | Type  |
| ------ | ----- |
| Tony   | 1.0.2 |

### url  

> http://v.juhe.cn/weather/index



## type

> json 

### method 

> get 

### Request Params  

| 序号 | 名称     | 必填 | 类型   | 说明                                           |
| ---- | -------- | ---- | ------ | ---------------------------------------------- |
| 1    | cityname | Y    | string | 城市名或城市ID，如："苏州"，需要utf8 urlencode |
| 2    | dtype    | N    | string | 返回数据格式：json或xml,默认json               |
| 3    | format   | N    | int    | 未来7天预报(future)两种返回格式，1或2，默认1   |
| 4    | key      | Y    | string | 在个人中心->我的数据,接口名称上方查看          |



### Response Params  

| 名称    | 说明       |
| ------- | ---------- |
| code    | 状态码     |
| message | 错误信息   |
| data    | 返回的数据 |



#### 返回示例  

```
{
	"code":200,
	"message":"",
	"data":{
		"username":"kangbazi",
		"age":"18",
		"child":{
			"username":"",
		}
	}
}
```

### 错误 提示  

| 错误码 | 说明           |
| ------ | -------------- |
| HAHA   | 服务器响应失败 |
| TEST   | 数据已经存在   |





## 视图   

* CBV 
  * class-base-view   类处理请求  
* FBV   
  * function-base-view   方法、函数处理请求   



