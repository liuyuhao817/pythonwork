"""
采用版本迭代的方式来学习，便于对不同版本的优缺点进行对比和理解。
V1：不使用任何设计模式和单元测试框架 (线性模型)
V2：使用UnitTest管理用例
V3：使用方法封装的思想，对代码进行优化
V4：采用PO模式的分层思想对代码进行拆分
V5：对PO分层之后的代码继续优化
V6：PO模式深入封装，把共同操作提取封装到父类中，子类直接调用父类的方法

PO介绍：  PO: page(页面) object(对象)
PO是Page Object的缩写，PO模式是自动化测试项目开发实践的最佳设计模式之一。
核心思想是通过对界面元素的封装减少冗余代码，同时在后期维护中，若元素定位发生变化， 只
需要调整页面元素封装的代码，提高测试用例的可维护性、可读性。
PO模式可以把一个页面分为三层，对象库层、操作层、业务层。
    对象库层：封装定位元素的方法。
    操作层：封装对元素的操作。
    业务层：将一个或多个操作组合起来完成一个业务功能。比如登录：需要输入帐号、密码、点击登录三个操作。
v4:实际中的po模式编写
结构：
    1.base（基类）：page页面一些公共的方法；
    2.page(页面对象)：一个页面封装成一个对象；继承base;
    3.scripts（业务层）：导包调用 page页面
PO模式优势：减少冗余代码   业务代码和测试代码被分开，降低耦合性   维护成本低
"""