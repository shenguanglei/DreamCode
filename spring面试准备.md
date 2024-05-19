## 1、谈谈Spring IOC的理解，原理与实现

总：

控制反转：理论思想，原来的对象是由使用者控制，有了spring后，可以把整个对象交给spring来帮助我们进行管理

DI依赖注入:把对应的属性的值注入到具体的对象中，@Autowired。PopulateBean完成属性值的注入

整个bean的生命周期，从创建到使用到销毁的过程，全部都是有容器来管理bean的生命周期

 分：

1、一般聊ioc容器的时候要涉及到容器的创建过程（beanFactory,DefaultListableBeanFactory）,向bean工厂中设置参数（BeanPostProcessor,Aware接口的子类）等等属性

2、加载解析bean对象，准备要创建的bean对象的定义对象beanDefinition,(xml或者注解的解析过程)

3、beanfactoryPostProcessor的处理，此处是扩展点，

PlaceHolderconfigurSupport,ConfigurationClassPostProcessor

4、BeanPostProcessor的注册功能，方便后续对bean对象完成具体的扩展功能

5、通过反射的方式讲BeanDefinition对象实例化成具体的bean 对象

6、bean对象的初始化过程（填充属性，调用aware子类的方法，调用BeanPostProcessor前置处理方法，调用init-method方法，调用BeanPostProcessor的后置处理方法）

## 2、谈一下Spring IOC的底层实现

底层实现：工作原理，过程、数据结构、流程设计模式，设计思想

你对他的理解和你了解的过的实现过程

反射、工厂、设计模式（关键的几个方法）

createBeanFactory

getBean,doGetBean,createBean,doCreateBEan,createBeanInstance(getDeclaredConstructor,newinstance),populateBean,initializingBean

1、先通过createBeanFactory 创建出一个Bean工厂（DefaultListableBeanFactory）

2、开始循环创建对象，因为容器中的bean默认都是单例的，所以优先通过getBean,doGetBean从容器中查找，找不到的话

3、通过createBean,doCreateBean方法以反射的方式创建对象，一般情况下使用的是无参的构造方法（getDeclaredConstructor,newInstance）

4、进行对象的属性填充populateBean

5、进行其他的初始化操作（initializingBean）

## 3、spring的生命周期 

在表述的时候不要只说图中有的关键点，要学会扩展描述

1、实例化bean:反射的方式生成对象

2、填充bean的属性：populateBean(),循环依赖问题（三级缓存）

3、调用aware接口相关的方法：invokeAwareMethod(完成BeanName,BeanFactory,BeanClassLoaderd对象的属性设置)

4、调用BeanPostProcessor中的前置处理方法：使用比较多的有（ApplicationContextPostProcessor,设置ApplicationContext,Environment,ResourceLoader,EmbeddValueResolver等对象）

5、调用init-method方法：invokeInitmethod(),判断是否实现了initializingBean接口，如果有，调用afterPropertiesSet方法，没有就不调用

6、调用BeanPostProcessor的后置处理方法：spring的aop就是在此处实现的，AbstractAutoProxyCreator注册Destuciton相关的回调接口：钩子函数

7、获取到完整的对象，可以通过getBean的方式来进行对象的获取

8、销毁流程，1：判断是否实现了DispoableBean接口2、调用destoryMethod方法



## 4.Spring是如何解决循环依赖的问题的

三级缓存、提前暴露对象、aop

总:什么是循环依赖问题，A依赖B、B依赖A

分：先说明bean的创建过程：实例化，初始化（填充属性）

1、先创建A对象，实例化A对象，此时A对象中的b属性为空，填充属性b

2、从容器中查找B对象，如果找到了，直接赋值不存在循环依赖问题（不通），找不到直接创建B对象

3、实例化B对象，此时B对象中的a属性为空，填充属性a

4、从容器中查找到A对象，找不到，直接创建

形成闭环的原因

此时，如果仔细琢磨的话，会发现A对象是存在的，只不过此时的A对象不是一个完整的状态，只完成了实例化但是未完成初始化，如果在程勋调用过程中，拥有了某个对象的引用，能否在后期给他完成赋值操作，可以优先把非完整的状态的对象优先赋值，等待后续操作来完成赋值，相当于提前暴露了某个不完整的对象引用，所以解决问题的核心在于实例化和初始化分开操作，这也是解决循环依赖问题的关键 

当所有的对象都完成实例化和初始化操作之后，还要把完整的对象放到容器中。此时容器中存在的对象的几个状态完成初始化=但未完成初始化，完整状态，因为都在容器中，所以要使用不同的map结构来进行存储，此时就有了一级缓存和二级缓存。如果一级缓存中有了，那么二级缓存中就不会存在同名的对象，因为他们的查找顺序是1、2、3，这样的方式来查找的。一级缓存中放的是完整对象，二级缓存中放的是非完整对象。

为什么需要三级缓存？三级缓存的value 类型是ObjectFactory是一个函数式接口，存在的意义是保证在整个容器运行过程中同名的bean对象只有一个

### 4、1缓存的放置时间和删除时间

三级缓存：createBeanInstance之后：addSingletonFactory

二级缓存：第一次从三级缓存确定对象是代理对象还是普通对象的时候，同时删除三级缓存getSingleton

一级缓存：生成完成对象之后放到一级缓存，删除二三级缓存：addSingleton

## 5、BeanFactory 和FactoryBean 有什么区别

相同点：都是用来创建bean对象的

不同点：使用BeanFactory创建对象的时候，必须要遵循严格的 生命周期流程、太复杂了，，如果想要简单的自定义某个对象的创建，同时创建完成的对象想交给spring 来管理，那么就需要实现FactoryBean接口了

isSingleton:是否是单例对象

getObjectType:获取返回对象的类型

getObject:自定义创建对象的过程（new ,反射，动态代理）

## 6、Spring中用到的设计模式

单例模式：bean默认都是单例的

原型模式：指定作用域为prototype

工厂模式：beanFactory

模板方法：postProcessBeanFactory、onRefresh,

initPropertvValue

## 7、Spring的aop的底层实现原理动态代理。

AOP是IOC的一个扩展功能，是先有IOC，再有的aop，只是在IOC的整个流程中新增一个扩展点而已，BeanPostProcessor。

总:aop概念,应用场景,动态代理

分:Bean的创建过程中，有一个步骤可以对Bean进行拓展实现, aop本身就是一个扩展功能，所以在BeanPostProcessor的后置处理方法中来进行实现

1、代理对象的创建过程（advice,切面，切点）

2、通过GDK或者是CGLIB方式来生成代理对象

3、在执行方法调用的时候，会调用到生成字节码文件中，直接会找到dynamicAdvisoredInterceptorl类中的intercept方法，从此方法开始执行，

4、根据之前定义好的通知来生成拦截器链，

5、从拦截器链中依次获取每一个个通知开始执行。在执行过程中，为了方便找到下一个通知是哪个，会有一个CglibMethodInvocation的对象,找到的时候是从-1的位置一次开始查找并执行的

## 8、Spring的事务是如何回滚的？

Spring的事务管理是如何实现的？

总、Spring的事务是由AOP来实现的。首先要生成具体的代理对象，然后按照AOP整套流程来执行具体的操作逻辑，正常情况下。要通过通知来完成核心功能，但事物不是通过通知来实现的，而是通过一个TransactionInterceptor来实现的。然后通过invoke来实现具体的逻辑。

分：

1、先准备工作，解析各个方法，让事物相关的属性，根据具体的属性来判断是否开始新事物，

2、当需要开启的时候获取。数据库连接关闭自动提交功能开启事务

3、执行具体的sql操作。

4、在回操作过程中，如果执行失败了，那么就会通过complete transactions after throwing看来完成事务的回滚操作。回滚的具体逻辑是通过do roll back方法来实现，实现的时候也是要先获取连接对象，通过连接对象来回滚。

5、如果执行过程中没有任何意外情况的发生那么通过commit transaction after returning来完成事务的提交操作，提交的具体逻辑是通过doCommit方法来实现的，实现的时候也是要获取连接，通过连接对象来提交

6、当事务执行完毕之后需要清理相关的事务信息cleanupTranscationInfo,如果想要聊得更加细致的话，需要知道TransationInfo,TransationStatus

## 9、谈一下spring 事务传播

传播特性有几种？7种

Required,Requires,new,nested,Support,Not_Support,Never,Mandatory

某一个事务嵌套另一个事务的时候怎么办

A方法调用B方法AB，方法都有事务，并且传播特性不同，那么a如果有异常，B怎么办？B如果有异常，A怎么办？

事务的传播特性指的是不同方法的嵌套调用过程中，事务应该如何进行处理，是用同一个事务，还是不同的事务。当出现异常的时候会回滚还是提交，两个方法之间的相关影响。在日常工作中使用比较多的是required requires_new,nested

分：1、先说事务的不同分类，可以分为三类：支持当前事务，不支持当前事务，嵌套事务

2、如果外层方法是requried,内层方法是，required requires_new,nested

2、如果外层方法是requires_new,内层方法是，required requires_new,nested

2、如果外层方法是nested,内层方法是，required requires_new,nested