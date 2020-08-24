# cookie和session

1. cookie：在网站中，http请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求是哪个用户。`cookie`的出现就是为了解决这个问题，第一次登录后服务器返回一些数据（cookie）给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的`cookie`数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个了。`cookie`存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过4KB。因此使用`cookie`只能存储一些小量的数据。
2. session: session和cookie的作用有点类似，都是为了存储用户相关的信息。不同的是，`cookie`是存储在本地浏览器，`session`是一个思路、一个概念、一个服务器存储授权信息的解决方案，不同的服务器，不同的框架，不同的语言有不同的实现。虽然实现不一样，但是他们的目的都是服务器为了方便存储数据的。`session`的出现，是为了解决`cookie`存储数据不安全的问题的。
3. cookie和session使用：`web`开发发展至今，`cookie`和`session`的使用已经出现了一些非常成熟的方案。在如今的市场或者企业里，一般有两种存储方式：
   - 存储在服务端：通过`cookie`存储一个`sessionid`，然后具体的数据则是保存在`session`中。如果用户已经登录，则服务器会在`cookie`中保存一个`sessionid`，下次再次请求的时候，会把该`sessionid`携带上来，服务器根据`sessionid`在`session`库中获取用户的`session`数据。就能知道该用户到底是谁，以及之前保存的一些状态信息。这种专业术语叫做`server side session`。`Django`把`session`信息默认存储到数据库中，当然也可以存储到其他地方，比如缓存中，文件系统中等。存储在服务器的数据会更加的安全，不容易被窃取。但存储在服务器也有一定的弊端，就是会占用服务器的资源，但现在服务器已经发展至今，一些`session`信息还是绰绰有余的。
   - 将`session`数据加密，然后存储在`cookie`中。这种专业术语叫做`client side session`。`flask`框架默认采用的就是这种方式，但是也可以替换成其他形式。

## flask中使用cookie和session



`cookies`：在Flask中操作cookie，是通过response对象来操作，可以在response返回之前，通过response.set_cookie来设置，这个方法有以下几个参数需要注意：
`key`：设置的cookie的key。
`value`：key对应的value。
`max_age`：改cookie的过期时间，如果不设置，则浏览器关闭后就会自动过期。
`expires`：过期时间，应该是一个datetime类型。
`domain`：该cookie在哪个域名中有效。一般设置子域名，比如cms.example.com。
`path`：该cookie在哪个路径下有效。
`session`：Flask中的session是通过from flask import session。然后添加值key和value进去即可。并且，Flask中的session机制是将session信息加密，然后存储在cookie中。专业术语叫做client side session。